[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![release](https://img.shields.io/github/downloads/Neur0tek/Jetson-Face-Follow/total.svg)

# Jetson-Face-Follow ( /!\ WORK IN PROGRESS /!\ ) 
Simple face follower for the Nvidia Jetson using OpenCV and InMoov eye mechanism

![gif](README/negif.gif)


## Material 

* Nvidia Jetson Nano 
* SD Card 64go 
* Pi Camera v2 (IMX219 sensor)
* Adafruit PCA9685
* MG90S Servo
* InMoov Eye Mechanisme (Optional)

## Wiring
```
PCA        Jetson
GND <----> GND
OE  <----> NC
SCL <----> SCL (PIN 28)
SDA <----> SDA (PIN 27)
Vcc <----> 3.3V
V+  <----> NC

Connect MG90S servo to Channel 0 of the PCA9685
```

## Installation

First install the dependencies : 
```bash
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
sudo apt-get install python3-dev
sudo pip install adafruit-pca9685
sudo pip install imutils
```
Add user to the i2c group : 

```bash
sudo usermod -a -G i2c username
sudo reboot
```

Check that your user is into the i2c group with the command `groups`

![groups](https://user-images.githubusercontent.com/36542615/60292686-fb41b700-991d-11e9-84a7-5543681a7f13.png)

Verify if the PCA9685 board is detected ( be sure to select the correct i2c bus on your nano ) :
```bash
i2cdetect -y -r 0
```
The device should be detected as 0x40 as below : 

![i2cdetect](https://user-images.githubusercontent.com/36542615/60295542-478ff580-9924-11e9-876b-ab71701c178f.png)

## Usage 

```bash
python3 JetsonCvPCA.py WIDTH HEIGHT 

ex. python3 JetsonCvPCA.py 640 480
```

![face_follow](https://user-images.githubusercontent.com/36542615/60295454-013a9680-9924-11e9-9129-40982a8e7d27.png)

### Informations

This is just a quick proof of concept , there is still a lot of improvements to do in order to have it to work faster.
I will do my best in order to keep the code updated ;-) 
