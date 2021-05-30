import pygame, time
from audioplayer import AudioPlayer
import RPi.GPIO as GPIO

# # re-map the bins on the board using bcm mode
# GPIO.setmode(GPIO.BCM)
#
# # set up each channel as an input or output
# GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

# define the strike objects that specify the sound file and light pattern

pygame.init()

strikes = [
    {
        'thunder' : "thunder-01.mp3",
        'patterns' :   [0,0,0,2,0,0,0,2,0,0,0,0],
        'description':  "A series of small flickers."
    },
    {
        'thunder' : "thunder-02.mp3",
        'patterns' : [1,2,0,0,0,0,0,0,0,0],
        'description' :   "Starts with a boom and then flickers"
    },
    {
        'thunder' : "thunder-03.mp3",
        'patterns' : [0,0,0,2,0,0,0,2,0,0,0,0],
        'description' :   "Starts with a boom and then flickers"
    },
    # {
    #     'thunder' : "thunder-04.mp3",
    #     'lightning' :   "pattern 4"
    # },
    # {
    #     'thunder' : "thunder-05.mp3",
    #     'lightning' :   "pattern 5"
    # },
    # {
    #     'thunder' : "thunder-06.mp3",
    #     'lightning' :   "pattern 6"
    # },
    # {
    #     'thunder' : "thunder-07.mp3",
    #     'lightning' :   "pattern 7"
    # },
    # {
    #     'thunder' : "thunder-08.mp3",
    #     'lightning' :   "pattern 8"
    # },
    # {
    #     'thunder' : "thunder-09.mp3",
    #     'lightning' :   "pattern 9"
    # },

]

patterns = [
    {
        'name'  : "flicker",
        'flash' : .25,
        'pause' :   .25
    },
    {
        'name'  :   "boom",
        'flash' :   2,
        'pause' :   .25
    },
    {
        'name'  :   "pause",
        'flash' :   0,
        'pause' :   1
    },

]

def flash():
    print("flash")
    # GPIO.output(17, GPIO.HIGH)

def pause():
    print("pause")
    # GPIO.output(17, GPIO.LOW)

# loop through each strike object

while True:
    for strike in strikes:

        secondsPassed = 0
        startTime = time.time()

        # play the sound file and trigger the relay according to the strike object's light pattern

        file = "Sounds/" + strike['thunder']
        print("playing thunder track: " + file)

        secondsPassed = time.time() - startTime

        print("seconds passed: " + str(round(secondsPassed,2)))

        # player = AudioPlayer(file)
        # player.play()

        print("flashing light pattern: " + strike['description'])

        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        for pattern in strike['patterns']:
            print(patterns[pattern]['name'])
            flash()
            time.sleep(patterns[pattern]['flash'])

            pause()
            time.sleep(patterns[pattern]['pause'])

        secondsPassed = time.time() - startTime
        print("seconds passed: " + str(round(secondsPassed,2)))

        thunderDuration = 10

        timeRemaining = thunderDuration - secondsPassed

        if(timeRemaining < thunderDuration):
            time.sleep(timeRemaining)

        pygame.mixer.music.stop()
        # player.stop()
        secondsPassed = 0

GPIO.cleanup()
