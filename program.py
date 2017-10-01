import RPi.GPIO as GPIO
import time
import os
from ayar import *
from derece import *
sensor = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_UP)

previous_state = False
current_state = False

while True:
    time.sleep(0.1)
    #print(datetime.datetime.now().minute)
    #print(temperature)
    
    if temperature>24 or (datetime.datetime.now().minute==54 and datetime.datetime.now().second<=5):
            os.system("python /home/pi/uyari.py")
            time.sleep(10)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        print GPIO.input(sensor)
        if GPIO.input(sensor) == 1:
                print zaman1
                print zaman2
                new_state = "HIGH" if current_state else "LOW"
                print("GPIO pin %s is %s" % (sensor, new_state))
                time.sleep(zaman1)
                os.system("fswebcam -r 640x480 -d /dev/video0 /home/pi/snapshot/webcam.jpg")
                time.sleep(zaman2)
                os.system("fswebcam -r 640x480 -d /dev/video0 /home/pi/snapshot/webcam1.jpg")
                os.system("python /home/pi/gonder.py")

