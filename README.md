# Jetson-Face-Follow
Simple face follower for the Nvidia Jetson using OpenCV and python3

## Material 

* Nvidia Jetson Nano 
* SD Card 64go 
* Pi Camera v2 (IMX219 sensor)
* Adafruit PCA9685


## Installation
```
sudo apt-get install python-smbus
sudo apt-get install i2c-tools
sudo apt-get install python-dev
sudo pip install adafruit-pca9685
sudo pip install imutils
sudo usermod -a -G i2c username
sudo reboot

```
## Usage 
```
python3 JetsonCvPCA.py WIDTH HEIGHT 

```
