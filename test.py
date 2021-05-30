import pygame, time
import RPi.GPIO as GPIO

# # re-map the bins on the board using bcm mode
GPIO.setmode(GPIO.BCM)

lightningPin = 17

#
# # set up each channel as an input or output
GPIO.setup(lightningPin, GPIO.OUT, initial=GPIO.LOW)

# define the strike objects that specify the sound file and light pattern

pygame.init()

# Duration is measured in seconds, where .1 = one tenth of one second.

def pause(duration):
    GPIO.setmode(lightningPin, LOW)
    time.sleep(duration)

def flash(duration):
    GPIO.setmode(lightningPin, HIGH)
    time.sleep(duration)
    GPIO.setmode(lightningPin, LOW)

def pulse(duration, length):
    pulseCount = duration / length

    i = 0
    while i < pulseCount:
        GPIO.setmode(lightningPin, HIGH)
        time.sleep(length)
        GPIO.setmode(lightningPin, LOW)
        time.sleep(length)
        i += 1

lightning = {
    'trackone' :   [
        # 1
        { 'action' : "pause",   'duration'  : .1 },
        { 'action' : "flash",   'duration'  : .2 },
        { 'action' : "crackle", 'duration'  : .6 },
        { 'action' : "flicker", 'duration'  : .1 },

        # 2
        { 'action' : "flicker", 'duration'  : .3 },
        { 'action' : "flash",   'duration'  : .2 },
        { 'action' : "crackle", 'duration'  : .2 },
        { 'action' : "flicker", 'duration'  : .3 },

        # 3
        { 'action' : "flash",   'duration'  : .2 },
        { 'action' : "crackle", 'duration'  : .2 },
        { 'action' : "flicker", 'duration'  : .3 },
        { 'action' : "pause",   'duration'  : .3 },

        # 4
        { 'action' : "flicker", 'duration'  : .3 },
        { 'action' : "pause",   'duration'  : .3 },
        { 'action' : "flicker", 'duration'  : .4 },

        # 5
        { 'action' : "flash",   'duration'  : .1 },
        { 'action' : "pause",   'duration'  : .4 },
        { 'action' : "flicker", 'duration'  : .3 },
        { 'action' : "pause",   'duration'  : .1 },
        { 'action' : "flash",   'duration'  : .1 },

        # 6
        { 'action' : "pause",   'duration'  : .5 },
        { 'action' : "flicker", 'duration'  : .3 },
        { 'action' : "pause",   'duration'  : .2 },

        # 7
        { 'action' : "flicker", 'duration'  : .2 },
        { 'action' : "flash",   'duration'  : .2 },
        { 'action' : "pause",   'duration'  : .2 },
        { 'action' : "flicker", 'duration'  : .2 },
        { 'action' : "pause",   'duration'  : .2 },

        # 8
        { 'action' : "crackle", 'duration'  : .3 },
        { 'action' : "pause",   'duration'  : .2 },
        { 'action' : "flicker", 'duration'  : .3 },
        { 'action' : "pause",   'duration'  : .2 },

        # 9
        { 'action' : "flicker", 'duration'  : .3 },
        { 'action' : "pause",   'duration'  : .5 },
        { 'action' : "flicker", 'duration'  : .1 },

        # 10
        { 'action' : "pause", 'duration'  : .3 }

    ]
}

strikes = [
    {
        'thunder' : "thunder-01.mp3",
        'patterns' :   [
            'flicker',
            'flicker',
            'boom',
            'flicker',
            'flicker',
            'flicker',
            'boom',
            'flicker',
            'flicker',
            'flicker'
        ],
        'description':  "A series of small flickers."
    },
    {
        'thunder' : "thunder-02.mp3",
        'patterns' : [

            1,2,0,0,0,0,0,0,0,0],
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

patterns = {
    'flicker' : {
        'flash' : .1,
        'pause' :   .1
    },
    'tinyFlicker' : {
        'flash' : .05,
        'pause' :   .05
    },
    'boom' : {
        'flash' : 2,
        'pause' :   .25
    },
    'pause' : {
        'flash' : .0,
        'pause' :   1
    }
}



def flash(length):
    print("flash")
    GPIO.output(lightningPin, GPIO.HIGH)
    time.sleep(length)
def pause(length):
    print("pause")
    GPIO.output(lightningPin, GPIO.LOW)
    time.sleep(length)
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

        print("flashing light pattern: " + strike['description'])

        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        # for pattern in strike['patterns']:
        #     print(patterns[pattern]['name'])
        #     flash(patterns[pattern]['flash'])
        #     # time.sleep(patterns[pattern]['flash'])
        #
        #     pause(patterns[pattern]['pause'])
        #     # time.sleep(patterns[pattern]['pause'])


        for strike in lightning.trackone:
            if (strike.action == "flash"):
                flash(strike.duration)
            elif (strike.action == "crackle"):
                pulse(strike.duration, .2)
            elif (strike.action == "flicker"):
                pulse(strike.duration, .1)
            else:
                pause(strike.duration)

        secondsPassed = time.time() - startTime
        print("seconds passed: " + str(round(secondsPassed,2)))

        thunderDuration = 10

        timeRemaining = thunderDuration - secondsPassed

        if(timeRemaining < thunderDuration):
            time.sleep(timeRemaining)

        pygame.mixer.music.stop()

        secondsPassed = 0

GPIO.cleanup()
