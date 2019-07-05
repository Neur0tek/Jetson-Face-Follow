#Face Follower for Nvidia Jetson Nano by Neurotek
#Code based on JetsonHacks article for the camera access : https://www.jetsonhacks.com/2019/04/02/jetson-nano-raspberry-pi-camera/  
#Connect MG90S servo to Channel 0 of the PCA9685
#WORK IN PROGRESS 

from __future__ import division
import cv2
import sys
from imutils.video import FPS
import time
import Adafruit_PCA9685

WIDTH  = 640
HEIGHT = 480

servo = Adafruit_PCA9685.PCA9685(address=0x40, busnum=0)
# Configure min and max servo pulse lengths
servo_min = 950 # Min pulse length out of 4096
servo_max = 1350 # Max pulse length out of 4096

face_cascade = cv2.CascadeClassifier('/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')



def welcome():
    
    if len (sys.argv) != 3 :
       print("**************************************************************************")
       print("\nWARN]Usage: Face_detect.py WIDTH HEIGHT \n")
       print("**************************************************************************")
       sys.exit(1)

    
    print ("[******************FACE FOLLOWING DETECTION*******************]")
    print ("[Detect and follow faces with Nvidia Jetson Nano              ]")
    print ("[Author : Neurotek                                            ]")
    print ("[Licensed under GNU GENERAL PUBLIC LICENSE (GPLv3)            ]")
    print ("[Version 1.0 (2019)                                           ]")
    print ("[*************************************************************]")


def gstreamer_pipeline (capture_width=WIDTH, capture_height=HEIGHT, display_width=WIDTH, display_height=HEIGHT, framerate=60, flip_method=0) :   
    return ('nvarguscamerasrc ! ' 
    'video/x-raw(memory:NVMM), '
    'width=(int)%d, height=(int)%d, '
    'format=(string)NV12, framerate=(fraction)%d/1 ! '
    'nvvidconv flip-method=%d ! '
    'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
    'videoconvert ! '
    'video/x-raw, format=(string)BGR ! appsink'  % (capture_width,capture_height,framerate,flip_method,display_width,display_height))


welcome()

servo.set_pwm_freq(60)


#################### Choix Resolution ############################
w1= int(sys.argv[1])
h1 = int(sys.argv[2])

if w1 == 1080 :
    WIDTH = w1
    print("[INFO] Width set to 1080")
elif w1 == 640 :
    WIDTH = w1
    print("[INFO] Width set to 640")
else : 
    print("[WARN] DEFAULT VALUE AUTO SET !")

if h1 == 720 :
    HEIGHT = h1
    print("[INFO] Height set to 720")
elif h1 == 480 :
    HEIGHT = h1
    print("[INFO] Height set to 480")
else : 
    print("[WARN] DEFAULT VALUE AUTO SET !")

#################### Webcam Warmup ################################
#print(gstreamer_pipeline(flip_method=2))
cap = cv2.VideoCapture(gstreamer_pipeline(capture_width=WIDTH, capture_height=HEIGHT, display_width=WIDTH, display_height=HEIGHT, flip_method=2), cv2.CAP_GSTREAMER)
print("[INFO] Warming video sensor...")
time.sleep(3.0)

fps = FPS().start()

if cap.isOpened():

    window_handle = cv2.namedWindow('Neurotek Face Detect', cv2.WINDOW_AUTOSIZE)
    
    while cv2.getWindowProperty('Neurotek Face Detect',0) >= 0:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:
        
                roi_color = img[y:y+h, x:x+w] #Region d interet ( visage couleur)

                ###################### Dessiner le rectangle #######################################
                color= (250, 0, 0) #BGR
                stroke = 2
                end_coord_x = x + w
                end_coord_y = y + h
                cv2.rectangle(img, (x, y), (end_coord_x, end_coord_y), color, stroke)

                ###################### Face follower ################################################
                if x < ((WIDTH/2)-x):
                    print("[TARGET] Left")
                    servo.set_pwm(0, 0, servo_min)
                    time.sleep(1)
                elif x > (WIDTH/2) :
                    print("[TARGET] Right")
                    servo.set_pwm(0, 0, servo_max)
                    time.sleep(1)
                else:
                    print("[TARGET] Straight")
                    servo.set_pwm(0, 0, 1150)
                    time.sleep(1)
            cv2.imshow('Neurotek Face Detect',img) 
            fps.update()       
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("[INFO] Quitting...")
                break
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    cap.release()
    cv2.destroyAllWindows()

else:
    print("[FATAL]Unable to open camera\nQuitting now ...")




