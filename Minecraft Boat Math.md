```java

public void tick() {  
    this.oldStatus = this.status;  
    this.status = this.getStatus();  
    if (this.status != AbstractBoat.Status.UNDER_WATER && this.status != AbstractBoat.Status.UNDER_FLOWING_WATER) {  
        this.outOfControlTicks = 0.0F;  
    } else {  
        this.outOfControlTicks++;  
    }  
  
    if (!this.level().isClientSide && this.outOfControlTicks >= 60.0F) {  
        this.ejectPassengers();  
    }  
  
    if (this.getHurtTime() > 0) {  
        this.setHurtTime(this.getHurtTime() - 1);  
    }  
  
    if (this.getDamage() > 0.0F) {  
        this.setDamage(this.getDamage() - 1.0F);  
    }  
  
    super.tick();  
    this.tickLerp();  
    if (this.isControlledByLocalInstance()) {  
        if (!(this.getFirstPassenger() instanceof Player)) {  
            this.setPaddleState(false, false);  
        }  
  
        this.floatBoat();  
        if (this.level().isClientSide) {  
            this.controlBoat();  
            this.level().sendPacketToServer(new ServerboundPaddleBoatPacket(this.getPaddleState(0), this.getPaddleState(1)));  
        }  
  
        this.move(MoverType.SELF, this.getDeltaMovement());  
    } else {  
        this.setDeltaMovement(Vec3.ZERO);  
    }  
  
    this.applyEffectsFromBlocks();  
    this.applyEffectsFromBlocks();  
    this.tickBubbleColumn();
```



```java
private void controlBoat() {  
    if (this.isVehicle()) {  
        float f = 0.0F;  
        if (this.inputLeft) {  
            this.deltaRotation--;  
        }  
  
        if (this.inputRight) {  
            this.deltaRotation++;  
        }  
  
        if (this.inputRight != this.inputLeft && !this.inputUp && !this.inputDown) {  
            f += 0.005F;  
        }  
  
        this.setYRot(this.getYRot() + this.deltaRotation);  
        if (this.inputUp) {  
            f += 0.04F;  
        }  
  
        if (this.inputDown) {  
            f -= 0.005F;  
        }  
  
        this.setDeltaMovement(  
            this.getDeltaMovement()  
                .add(  
                    (double)(Mth.sin(-this.getYRot() * (float) (Math.PI / 180.0)) * f),  
                    0.0,  
                    (double)(Mth.cos(this.getYRot() * (float) (Math.PI / 180.0)) * f)  
                )  
        );  
        this.setPaddleState(this.inputRight && !this.inputLeft || this.inputUp, this.inputLeft && !this.inputRight || this.inputUp);  
    }  
}
```