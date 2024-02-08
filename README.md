# RPi_FLH
Python3 implementation for a RPi FAN+LCD HAT with good features.

LCD displays IP address and FAN status.<br>
FAN on/off state controlled by CPU temp.

## Language:
Python3

## Dependencies:
pil<br>
RPi.GPIO<br>
smbus


## Install deps:
sudo apt update<br>
sudo apt install python3-pil<br>
sudo apt install python3-RPi.GPIO<br>
sudo apt install python3-smbus

## I2C needs to be enabled for smbus functionality.
sudo raspi-config<br>
  -Option 3 "Interface Options"<br>
    -Option I4 "I2C"<br>
      Yes<br>

