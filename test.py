# import pygame, time
import time
import RPi.GPIO as GPIO

# set up the relay pins

# GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
#
# RELAIS_1_GPIO = 17
# GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
# GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
# GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on

# re-map the bins on the board using bcm mode
GPIO.setmode(GPIO.BCM)

# set up each channel as an input or output
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)


GPIO.output(17, GPIO.HIGH)

# time.sleep(0.25)
time.sleep(1)


GPIO.output(17, GPIO.LOW)

# GPIO.output(17, GPIO.LOW)
# GPIO.output(17, GPIO.HIGH)


GPIO.cleanup()

# define the strike objects that specify the sound file and light pattern

# pygame.init()
#
# strikes = [
#     {
#         'thunder' : "thunder-01.mp3",
#         'lightning' :   "pattern 1"
#     },
#     {
#         'thunder' : "thunder-02.mp3",
#         'lightning' :   "pattern 2"
#     },
#     {
#         'thunder' : "thunder-03.mp3",
#         'lightning' :   "pattern 3"
#     },
#     {
#         'thunder' : "thunder-04.mp3",
#         'lightning' :   "pattern 4"
#     },
#     {
#         'thunder' : "thunder-05.mp3",
#         'lightning' :   "pattern 5"
#     },
#     {
#         'thunder' : "thunder-06.mp3",
#         'lightning' :   "pattern 6"
#     },
#     {
#         'thunder' : "thunder-07.mp3",
#         'lightning' :   "pattern 7"
#     },
#     {
#         'thunder' : "thunder-08.mp3",
#         'lightning' :   "pattern 8"
#     },
#     {
#         'thunder' : "thunder-09.mp3",
#         'lightning' :   "pattern 9"
#     },
#
# ]
#
# # loop through each strike object
#
# while True:
#     for strike in strikes:
#
#         # play the sound file and trigger the relay according to the strike object's light pattern
#
#         print("playing thunder track: " + strike['thunder'])
#         print("flashing light pattern: " + strike['lightning'])
#         #playsound("Sounds/" + strike['thunder'])
#         pygame.mixer.music.load("Sounds/" + strike['thunder'])
#         pygame.mixer.music.play()
#         time.sleep(10)
#         pygame.mixer.music.stop()
