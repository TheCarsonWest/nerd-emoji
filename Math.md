# The mathematics behind boat racing
# How do we move in a straight line?
Heres a pseudocode breakdown of how boat physics works in Minecraft(if you only worry about going in a straight line):
```java
public void tick(){ // Every tick, this runs (Yes, its all tick based!)
	if (wIsPressed()) { // If W is pressed, add thrust
		t = .04
	}else{
		if(sIsPressed()) { // If S is pressed, subtract thrust
			t = .005
		}else{
			if(aIsPressed || dIsPressed){ // If you are turning but NOT moving forward or backward, add a little bit of thrust
				t = .005
			}
		}
		
	}
	newVelocity = (oldVelocity+t) * friction
}
```
## Basic breakdown
If we just hold W, while on a block with friction value $f$, we can find our velocity at tick $t$ using this recursive series.
## $$v_t=(v_{t-1}+.04)\times f$$
Which can be generalized as an equation (this is very useful):
## $$v(t)=\frac{.04f}{1-f}(1-f^t)$$
Graphing on desmos yields this line.
![[Pasted image 20260218134005.png]]
## Friction values and top speed.
This equation has an asymptote, indicating the speed we will reach after an infinite amount of time, specifically at  $$\frac{.04f}{1-f} \space\text{ blocks/tick}$$or in the metric we like, 
$$v_{max}(f)= 20\left(\frac{.04f}{1-f}\right) \space\text{ blocks/second}$$
Plugging this in with the friction values we commonly use we find we find 
$$v_{max}(0.989 \text{ (Blue Ice) })=71.93 \frac{\text{blocks}}{\text{sec}}$$$$v_{max}(0.98 \text{ (Regular and Packed Ice) })=39.2 \frac{\text{blocks}}{\text{sec}}$$
Its a little smaller than what has been found experimentally, but close enough.

### Finding a friction for for a certain top speed
rearranging the equation we can find the required friction value for a certain top speed(in blocks/tick), which could be useful on maps using boatutils, we get this equation

$$f(v_{max})=\frac{20v_{max}}{20(v_{max}+.04)}$$
so for example, if we wanted to find the friction value to limit the player to 20 blocks/second, or 1 block/tick, 
$$f\left( \frac{20}{20} \right)=0.962$$