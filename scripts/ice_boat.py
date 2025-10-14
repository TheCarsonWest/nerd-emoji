import pygame
import math
from PIL import Image
import keyboard

# --- Game Constants (Minecraft-derived) ---
TICK_RATE = 20  # Minecraft ticks per second
PHYSICS_TICK_DURATION = 1.0 / TICK_RATE # Duration of one Minecraft physics tick in seconds

# Rendering scale
PIXELS_PER_BLOCK = 20 # How many screen pixels represent one Minecraft block

# Boat Physics Constants
A_THRUST = 0.04  # Forward acceleration in blocks/tick (positive value)
F_FRICTION_BLUE_ICE = 0.989 # Horizontal velocity damping factor (invFriction)
F_FRICTION_PACKED_ICE = 0.980 # Packed Ice friction
F_FRICTION_NORMAL_BLOCK = 0.600 # Default block friction (e.g., dirt)

# Turning speed (deltaRotation increment/decrement)
TURN_RATE_INPUT = 1.0 # Degrees per tick when A/D is pressed

# Boat Hitbox (Minecraft's boat is 1.375 blocks wide, 1.375 blocks long)
BOAT_HITBOX_SIZE = 1.375 # Blocks

# --- Pygame Setup ---
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
TARGET_FPS = 120 

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minecraft Boat on Ice Track")
clock = pygame.time.Clock() # CORRECTED: Assign pygame.time.Clock() to 'clock'

# --- Colors ---
BLUE_ICE_COLOR = (76, 127, 213) # 4C7FD5
PACKED_ICE_COLOR = (101, 140, 210) # 658CD2
OTHER_BLOCK_COLOR = (50, 50, 50) # Dark gray for non-ice blocks
BOAT_COLOR = (200, 100, 50) # Brownish
VELOCITY_COLOR = (255, 0, 0) # Red
HITBOX_COLOR = (0, 255, 0) # Green for hitbox outline
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 24)

# --- Map Loading and Block Friction Mapping ---
MAP_IMAGE_PATH = "boat_map.png"
try:
    map_img = Image.open(MAP_IMAGE_PATH).convert("RGB")
    MAP_WIDTH_BLOCKS = map_img.width
    MAP_HEIGHT_BLOCKS = map_img.height
    map_pixels = list(map_img.getdata()) # Flat list of (R,G,B) tuples

    # Convert flat list to 2D array for easier access
    GAME_MAP = []
    for y in range(MAP_HEIGHT_BLOCKS):
        row = []
        for x in range(MAP_WIDTH_BLOCKS):
            row.append(map_pixels[y * MAP_WIDTH_BLOCKS + x])
        GAME_MAP.append(row)

    # Map color to friction value
    BLOCK_FRICTIONS = {
        BLUE_ICE_COLOR: F_FRICTION_BLUE_ICE,
        PACKED_ICE_COLOR: F_FRICTION_PACKED_ICE,
        # Any other color in the map will default to F_FRICTION_NORMAL_BLOCK
    }
    # Ensure all colors in the map have a friction defined, or default to F_FRICTION_NORMAL_BLOCK
    for y in range(MAP_HEIGHT_BLOCKS):
        for x in range(MAP_WIDTH_BLOCKS):
            color = GAME_MAP[y][x]
            if color not in BLOCK_FRICTIONS:
                BLOCK_FRICTIONS[color] = F_FRICTION_NORMAL_BLOCK 

except FileNotFoundError:
    print(f"Error: {MAP_IMAGE_PATH} not found. Please create a map image named 'boat_map.png'.")
    pygame.quit()
    exit()
except Exception as e:
    print(f"Error loading map: {e}")
    pygame.quit()
    exit()

# --- Boat Class ---
class Boat:
    def __init__(self, start_x, start_y):
        # Current Physics State
        self.x = start_x # Initial position in blocks
        self.y = start_y
        self.vx = 0.0
        self.vy = 0.0
        # Yaw: 0=Right (+X), 90=Up (+Y), increases counter-clockwise (matches math.cos/sin)
        self.yaw = 90.0 - 21.1 # Your specific reference yaw
        self.delta_rot = 0.0

        # Previous Physics State (for interpolation)
        self.prev_x = start_x
        self.prev_y = start_y
        self.prev_yaw = self.yaw

        # Input States
        self.input_up = False
        self.input_left = False
        self.input_right = False

        # Status (always ON_LAND for this demo on a track)
        self.status = "ON_LAND"
        self.land_friction = F_FRICTION_BLUE_ICE # Initialized, will be updated by get_ground_friction
        self.inv_friction = self.land_friction # inv_friction is set from land_friction when ON_LAND

        # Rendering properties for a triangle boat
        # Front is along local +Y axis, so (0, 15) is the tip
        self.base_points = [
            (0, 15),    # Front tip (local +Y)
            (-10, -10), # Back left
            (10, -10)   # Back right
        ]

    def update_global_input(self):
        self.input_up = keyboard.is_pressed('w')
        self.input_left = keyboard.is_pressed('d')
        self.input_right = keyboard.is_pressed('a')

    def get_ground_friction(self):
        """Calculates the average friction of blocks under the boat's hitbox."""
        friction_sum = 0.0
        block_count = 0

        half_hitbox_x = BOAT_HITBOX_SIZE / 2.0
        half_hitbox_y = BOAT_HITBOX_SIZE / 2.0 

        # Define the area to check for blocks (similar to Minecraft's loop)
        min_check_x = math.floor(self.x - half_hitbox_x) - 1
        max_check_x = math.ceil(self.x + half_hitbox_x) + 1
        min_check_y = math.floor(self.y - half_hitbox_y) - 1
        max_check_y = math.ceil(self.y + half_hitbox_y) + 1

        # Simplified AABB for the boat's base for intersection check
        boat_aabb_min_x = self.x - half_hitbox_x
        boat_aabb_max_x = self.x + half_hitbox_x
        boat_aabb_min_y = self.y - half_hitbox_y
        boat_aabb_max_y = self.y + half_hitbox_y

        for block_x in range(int(min_check_x), int(max_check_x)):
            for block_y in range(int(min_check_y), int(max_check_y)):
                # Check for intersection between block (1x1) and boat's AABB
                block_intersects_boat = (
                    max(boat_aabb_min_x, block_x) < min(boat_aabb_max_x, block_x + 1) and
                    max(boat_aabb_min_y, block_y) < min(boat_aabb_max_y, block_y + 1)
                )

                if block_intersects_boat:
                    if 0 <= block_x < MAP_WIDTH_BLOCKS and 0 <= block_y < MAP_HEIGHT_BLOCKS:
                        block_color = GAME_MAP[block_y][block_x]
                        if block_color == (255, 255, 255): # Assuming white is empty/air
                            continue 
                        friction_sum += BLOCK_FRICTIONS.get(block_color, F_FRICTION_NORMAL_BLOCK)
                        block_count += 1
                    else:
                        # Treat out-of-bounds as normal blocks for friction purposes
                        friction_sum += F_FRICTION_NORMAL_BLOCK
                        block_count += 1

        if block_count == 0:
            return F_FRICTION_NORMAL_BLOCK # Default if no blocks found (e.g., floating)
        return friction_sum / float(block_count)

    def get_block_speed_factor(self):
        """Minecraft's getBlockSpeedFactor for ice is 1.0, effectively no additional damping."""
        return 1.0

    def tick(self):
        # Store current state as previous state for interpolation
        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_yaw = self.yaw

        # --- 0. Status Update (getStatus logic) ---
        # This part sets self.land_friction based on the blocks under the boat.
        # For this simulation, we assume ON_LAND, so inv_friction will be land_friction.
        self.land_friction = self.get_ground_friction() 
        self.inv_friction = self.land_friction 

        # --- 1. Float Boat Logic (Damping) ---
        # This applies damping FIRST to both linear and angular velocities.
        self.vx *= self.inv_friction
        self.vy *= self.inv_friction
        self.delta_rot *= self.inv_friction

        # --- 2. Control Boat Logic (Input Application & Yaw Update) ---
        # Calculate angular input (after damping)
        if self.input_left:
            self.delta_rot += TURN_RATE_INPUT # CCW turn in our yaw system
        if self.input_right:
            self.delta_rot -= TURN_RATE_INPUT # CW turn in our yaw system

        # Update yaw based on the now-modified delta_rot
        self.yaw += self.delta_rot
        self.yaw %= 360 # Keep yaw within 0-360 degrees
        yaw_rad = math.radians(self.yaw)

        # Calculate linear thrust input (after damping and based on NEW yaw)
        f_thrust_factor = 0.0
        if self.input_up:
            f_thrust_factor += A_THRUST # Positive for forward thrust
        # Add small turning thrust if only turning, but not if also moving forward/backward
        if (self.input_right != self.input_left) and (not self.input_up): # and not self.input_down (if implemented)
             f_thrust_factor += 0.005 # Minor thrust when just turning

        # Apply thrust to linear velocity (after damping)
        self.vx += math.cos(yaw_rad) * f_thrust_factor
        self.vy += math.sin(yaw_rad) * f_thrust_factor

        # --- 3. Move Logic (Position Update & Collision) ---
        self.x += self.vx
        self.y += self.vy

        # Simple boundary collision response
        half_hitbox_x = BOAT_HITBOX_SIZE / 2.0
        half_hitbox_y = BOAT_HITBOX_SIZE / 2.0

        collided_x = False
        collided_y = False

        if self.x < half_hitbox_x:
            self.x = half_hitbox_x
            collided_x = True
        elif self.x > MAP_WIDTH_BLOCKS - half_hitbox_x:
            self.x = MAP_WIDTH_BLOCKS - half_hitbox_x
            collided_x = True

        if self.y < half_hitbox_y:
            self.y = half_hitbox_y
            collided_y = True
        elif self.y > MAP_HEIGHT_BLOCKS - half_hitbox_y:
            self.y = MAP_HEIGHT_BLOCKS - half_hitbox_y
            collided_y = True
        
        # If clamped, kill velocity in that direction (similar to Minecraft's horizontalCollision)
        if collided_x:
            self.vx = 0
        if collided_y:
            self.vy = 0

        # --- 4. Block Speed Factor (End of Move Logic) ---
        # This is always 1.0 for ice blocks, so it does not change velocity here.
        self.vx *= self.get_block_speed_factor()
        self.vy *= self.get_block_speed_factor()


    def draw(self, surface, interpolation_alpha, camera_offset_x, camera_offset_y):
        # Interpolate position and yaw for smooth rendering
        render_x = self.prev_x + (self.x - self.prev_x) * interpolation_alpha
        render_y = self.prev_y + (self.y - self.prev_y) * interpolation_alpha
        
        delta_yaw = self.yaw - self.prev_yaw
        if delta_yaw > 180: delta_yaw -= 360
        elif delta_yaw < -180: delta_yaw += 360
        render_yaw = self.prev_yaw + delta_yaw * interpolation_alpha
        render_yaw %= 360

        # Convert interpolated block coordinates to screen pixels, applying camera offset
        pixel_x = int(render_x * PIXELS_PER_BLOCK - camera_offset_x)
        pixel_y = int(render_y * PIXELS_PER_BLOCK - camera_offset_y)

        # Draw boat (rotated triangle)
        center = (pixel_x, pixel_y)
        points = []
        # render_yaw is 0=Right, 90=Up (CCW).
        # base_points define front along local +Y.
        # To align local +Y with world +Y (when render_yaw=90), the rotation angle needs to be 0.
        # So, angle_rad = math.radians(render_yaw - 90) works.
        angle_rad = math.radians(render_yaw - 90) 
        for p in self.base_points:
            # Standard 2D rotation: (x', y') = (x*cos(angle) - y*sin(angle), x*sin(angle) + y*cos(angle))
            rotated_x = p[0] * math.cos(angle_rad) - p[1] * math.sin(angle_rad)
            rotated_y = p[0] * math.sin(angle_rad) + p[1] * math.cos(angle_rad)
            points.append((center[0] + rotated_x, center[1] + rotated_y))
        pygame.draw.polygon(surface, BOAT_COLOR, points)

        # Draw hitbox (green square)
        half_hitbox_pixels = (BOAT_HITBOX_SIZE / 2.0) * PIXELS_PER_BLOCK
        hitbox_rect = pygame.Rect(
            pixel_x - half_hitbox_pixels, 
            pixel_y - half_hitbox_pixels, 
            BOAT_HITBOX_SIZE * PIXELS_PER_BLOCK, 
            BOAT_HITBOX_SIZE * PIXELS_PER_BLOCK
        )
        pygame.draw.rect(surface, HITBOX_COLOR, hitbox_rect, 1) # 1 pixel wide outline

        # Draw velocity vector (use current physics velocity for display)
        vel_mag = math.sqrt(self.vx**2 + self.vy**2)
        if vel_mag > 0.01:
            # Scale velocity vector for visibility, cap length
            vec_length_pixels = min(vel_mag * PIXELS_PER_BLOCK * 5, 100) # Max 100 pixels
            vel_vec_end_x = pixel_x + (self.vx / vel_mag) * vec_length_pixels
            vel_vec_end_y = pixel_y + (self.vy / vel_mag) * vec_length_pixels
            pygame.draw.line(surface, VELOCITY_COLOR, center, (vel_vec_end_x, vel_vec_end_y), 2)

        # Draw info text (always at fixed screen position)
        speed_text = font.render(f"Speed: {vel_mag * TICK_RATE:.2f} blocks/s ({vel_mag:.3f} b/tick)", True, TEXT_COLOR)
        yaw_text = font.render(f"Yaw: {self.yaw:.1f}° (Render: {render_yaw:.1f}°)", True, TEXT_COLOR)
        delta_rot_text = font.render(f"Delta Rot: {self.delta_rot:.2f}°/tick", True, TEXT_COLOR)
        friction_text = font.render(f"Friction: {self.inv_friction:.3f}", True, TEXT_COLOR)
        pos_text = font.render(f"Pos: ({self.x:.1f}, {self.y:.1f}) blocks", True, TEXT_COLOR)

        surface.blit(speed_text, (10, 10))
        surface.blit(yaw_text, (10, 30))
        surface.blit(delta_rot_text, (10, 50))
        surface.blit(friction_text, (10, 70))
        surface.blit(pos_text, (10, 90))

# --- Game Loop ---
# Specific starting point for reference
initial_boat_x = 290.253 
initial_boat_y = 281.557
boat = Boat(initial_boat_x, initial_boat_y) 

running = True
dt_accumulator = 0.0 # Accumulator for physics ticks
last_time = pygame.time.get_ticks() / 1000.0 # Time in seconds

while running:
    current_time = pygame.time.get_ticks() / 1000.0
    frame_time = current_time - last_time
    last_time = current_time
    
    dt_accumulator += frame_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    boat.update_global_input()

    # --- Physics Update Loop ---
    while dt_accumulator >= PHYSICS_TICK_DURATION:
        boat.tick()
        dt_accumulator -= PHYSICS_TICK_DURATION
        
    # --- Rendering ---
    screen.fill(OTHER_BLOCK_COLOR) # Background for areas outside map or non-ice

    # Calculate interpolation alpha (0.0 to 1.0) for smooth rendering
    interpolation_alpha = dt_accumulator / PHYSICS_TICK_DURATION

    # Calculate interpolated render position for camera centering
    render_x = boat.prev_x + (boat.x - boat.x) * interpolation_alpha # Interpolate between prev_x and x
    render_y = boat.prev_y + (boat.y - boat.y) * interpolation_alpha # Interpolate between prev_y and y

    # Camera offset to center the boat
    camera_offset_x = (render_x * PIXELS_PER_BLOCK) - (SCREEN_WIDTH / 2)
    camera_offset_y = (render_y * PIXELS_PER_BLOCK) - (SCREEN_HEIGHT / 2)

    # Determine visible tile range
    min_visible_block_x = max(0, int(camera_offset_x / PIXELS_PER_BLOCK) - 1)
    max_visible_block_x = min(MAP_WIDTH_BLOCKS, int((camera_offset_x + SCREEN_WIDTH) / PIXELS_PER_BLOCK) + 1)
    min_visible_block_y = max(0, int(camera_offset_y / PIXELS_PER_BLOCK) - 1)
    max_visible_block_y = min(MAP_HEIGHT_BLOCKS, int((camera_offset_y + SCREEN_HEIGHT) / PIXELS_PER_BLOCK) + 1)

    # Draw ONLY the visible map tiles
    for y in range(min_visible_block_y, max_visible_block_y):
        for x in range(min_visible_block_x, max_visible_block_x):
            block_color = GAME_MAP[y][x]
            screen_x = x * PIXELS_PER_BLOCK - camera_offset_x
            screen_y = y * PIXELS_PER_BLOCK - camera_offset_y
            pygame.draw.rect(screen, block_color, (screen_x, screen_y, PIXELS_PER_BLOCK, PIXELS_PER_BLOCK))
    
    boat.draw(screen, interpolation_alpha, camera_offset_x, camera_offset_y)
    
    pygame.display.flip()

    clock.tick(TARGET_FPS)

pygame.quit()