# RPi4_LCD_FAN_HAT
Python3 implementation for a RPi4 HAT containing LCD and Fan.

## Lang
Python3

## Dependencies:
pil
RPi.GPIO
smbus


## Install deps:
sudo apt update
sudo apt install python3-pil
sudo apt install python3-RPi.GPIO
sudo apt install python3-smbus

## I2C needs to be enabled for smbus functionality.
sudo raspi-config
  -Option 3 "Interface Options"
    -Option I4 "I2C"
      Yes

