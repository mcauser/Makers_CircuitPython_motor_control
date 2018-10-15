"""Motor control test"""
import time
import makers_motor_control

motors = makers_motor_control.MotorControl()

motors.set_throttle(0.0, 0.0)

while True:
    motors.set_throttle(0.5, 0.5, 0.25, True)   # forward
    motors.set_throttle(-0.5, -0.5, 0.25, True) # backward
    motors.set_throttle(0.0, 0.5, 0.25, True)   # left
    motors.set_throttle(0.5, 0.0, 0.25, True)   # right

    time.sleep(5.0)
