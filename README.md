[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


# Jetson-Face-Follow
Simple face follower for the Nvidia Jetson using OpenCV and python3

## Material 

* Nvidia Jetson Nano 
* SD Card 64go 
* Pi Camera v2 (IMX219 sensor)
* Adafruit PCA9685

## Wiring
```
PCA        Jetson
GND <----> GND
OE  <----> NC
SCL <----> SCL (PIN 28)
SDA <----> SDA (PIN 27)
Vcc <----> 3.3V
V+  <----> NC
```

## Installation

First install the dependencies : 
```bash
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
sudo apt-get install python-dev
sudo pip install adafruit-pca9685
sudo pip install imutils
```
Add user to the i2c group : 

```bash
sudo usermod -a -G i2c username
sudo reboot
```

Check that your user is into the i2c group with the command `groups`

Verify if the PCA9685 board is detected ( be sur to select the correct i2c bus on your nano ) :
```bash
i2cdetect -y -r 0
```

## Usage 

```bash
python3 JetsonCvPCA.py WIDTH HEIGHT 
```
