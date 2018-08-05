#import modules
import RPi.GPIO as GPIO
from time import sleep
import os
import picamera
import pytumblr
from fractions import Fraction

# send commands from Python to Linux shell
makeVid = "gm convert -delay 100 *.jpg joined.gif"

# variables to hold pin numbers 
led1 = 16
led2 = 21
button = 15

# authenticates via OAuth 
client = pytumblr.TumblrRestClient(
    'lxfsEd0tRSPFYjEymv92trQrJqynq2izOOkbNt2wO9EzkWEZfX',
    'DjhY2cP8yKigHLTRdDu8vMi1OdKOMS7foFKNolJRgyTUdq3V5M',
    'TQdWZj4k57ElbVIsssvGCAXDyK98sTPyCSAlztvTksw4Zou2Ik',  
    'l8sBVG8nSERZcj1WaH3PCQ4lca8fh97an8fhqLptkjiZQxak3s'
)

#set up GPIOs:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

camera = picamera.PiCamera() #initiate picamera module and class
camera.resolution = (640, 480) # set resolution of pics
camera.brightness = 60 #set brightness settings
camera.annotate_foreground = picamera.Color(y=0.2, u=0, v=0) #set color of annotation

try:
    #read button
    while True:
        GPIO.setmode(GPIO.BCM)
        if GPIO.input(button):
            print('Button pressed')
            sleep(0.2)
            # if pressed blink a led at two speeds
            for i in range(3):
                GPIO.output(led1, True)
                sleep(1)
                GPIO.output(led1, False)
                sleep(1)
            for i in range(3):
                GPIO.output(led1, True)
                sleep(.25)
                GPIO.output(led1, False)
                sleep(.25)
            # start camera preview
            camera.start_preview()
            # display text over preview screen
            camera.annotate_text = 'Get ready!'
            camera.annotate_text = '1'
            # take photos
            for i in range(5):
                camera.capture('/home/pi/image%s.jpg' % i)
                sleep(5)
                if i == 1:
                    camera.annotate_text = '2'
                elif i == 2:
                    camera.annotate_text = '3'
                elif i == 3:
                    camera.annotate_text = '4'
                if i == 4:
                    break
            camera.stop_preview()
            os.system(makeVid) #send command to convert images into GIF
            print('uploading')
                #upload photo to Tumblr
            client.create_photo(
            'emmanguyen28', #update username
            state="published",
            tags=["pi photobooth", "raspberry pi", "emma_nguyen"],
            data="/home/pi/joined.gif")
            print("uploaded")
            GPIO.output(led2, True)
            sleep(.25)
            GPIO.output(led2, False)
            
except KeyboardInterrupt: #hit Ctrl C to stop program
    print('program stopped')
finally:
    GPIO.cleanup() # cleanup GPIO channels



