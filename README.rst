Introduction
============

.. image:: https://readthedocs.org/projects/makers-circuitpython-motor-control/badge/?version=latest
    :target: https://makers-circuitpython-motor-control.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://travis-ci.org/fmorton/Makers_CircuitPython_motor_control.svg?branch=master
    :target: https://travis-ci.org/fmorton/Makers_CircuitPython_motor_control
    :alt: Build Status

CircuitPython helper for Circuit Playground Express/Crickit motor control

Examples of products to use this library with:

* `Circuit Playground Express <https://www.adafruit.com/product/3333>`_
* `Adafruit CRICKIT for Circuit Playground Express <https://www.adafruit.com/product/3093>`_


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython with Crickit support <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block:: python

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


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/fmorton/Makers_CircuitPython_MotorControl/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix makers-circuitpython-motor-control --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
