# The MIT License (MIT)
#
# Copyright (c) 2018 Frank Morton for Neighborhood Makers Inc
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`makers_motor_control`
====================================================

.. CircuitPython helper for crickit motor control

* Author(s): Frank Morton

Implementation Notes
--------------------

**Hardware:**

* `Circuit Playground Express <https://www.adafruit.com/product/3333>`_
* `Adafruit CRICKIT for Circuit Playground Express <https://www.adafruit.com/product/3093>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
  
"""

import time
from adafruit_crickit import crickit

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/fmorton/Makers_CircuitPython_motor_control.git"


"""
  Demo code for Circuit Playground Express + Crickit:


  import time
  import makers_motor_control

  motors = makers_motor_control.MotorControl()

  motors.set_throttle(0.0, 0.0)

  while True:
      motors.set_throttle(0.5, 0.5, 0.5, True)   # forward
      motors.set_throttle(-0.5, -0.5, 0.5, True) # backward
      motors.set_throttle(0.0, 0.5, 0.5, True)   # left
      motors.set_throttle(0.5, 0.0, 0.5, True)   # right

      time.sleep(5.0)
"""

class MotorControl:
    def __init__(self):
        self.left_motor = crickit.dc_motor_1
        self.right_motor = crickit.dc_motor_2


    def stop_motors(self):
        self.left_motor.throttle = 0.0
        self.right_motor.throttle = 0.0


    def set_throttle(self, left_motor_throttle, right_motor_throttle, sleep_amount = 0.0, stop_after_moving = False):
        self.left_motor.throttle = left_motor_throttle
        self.right_motor.throttle = right_motor_throttle
        if sleep_amount > 0.0:
            time.sleep(sleep_amount)
        if stop_after_moving:
            self.stop_motors()
