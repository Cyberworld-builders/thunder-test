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
    GPIO.output(lightningPin, GPIO.LOW)
    time.sleep(duration)

def flash(duration):
    GPIO.output(lightningPin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(lightningPin, GPIO.LOW)

def pulse(duration, length):
    pulseCount = duration / length

    i = 0
    while i < pulseCount:
        halfLength = length * .5
        GPIO.output(lightningPin, GPIO.HIGH)
        time.sleep(halfLength)
        GPIO.output(lightningPin, GPIO.LOW)
        time.sleep(halfLength)
        i += 1

strikes = [
    {
        'description' :   "Steady rumble with a few sort of peaks.",
        'thunderFile' : "thunder-01.mp3",
        'lightningPattern'  :   [

            # 1
            { 'action' : "pause",   'duration'  : .1 },
            { 'action' : "flash",   'duration'  : .3 },
            { 'action' : "crackle", 'duration'  : .4 },
            { 'action' : "flicker", 'duration'  : .2 },

            # 2
            { 'action' : "flicker", 'duration'  : .2 },
            { 'action' : "flash",   'duration'  : .3 },
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
            { 'action' : "flash",   'duration'  : .3 },
            { 'action' : "pause",   'duration'  : .4 },
            { 'action' : "flicker", 'duration'  : .3 },

            # 6
            { 'action' : "pause",   'duration'  : .5 },
            { 'action' : "flicker", 'duration'  : .3 },
            { 'action' : "pause",   'duration'  : .2 },

            # 7
            { 'action' : "flicker", 'duration'  : .2 },
            { 'action' : "flash",   'duration'  : .4 },
            { 'action' : "pause",   'duration'  : .1 },
            { 'action' : "flicker", 'duration'  : .2 },
            { 'action' : "pause",   'duration'  : .1 },

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
            { 'action' : "pause", 'duration'  : .1 }

        ]
    },
    {
        'description' :   "Starts with a boom and then flickers and fades.",
        'thunderFile' : "thunder-02.mp3",
        'lightningPattern'  :   [

            # 1, 2, & 3 Hesitates for nearly a second and then there's a big flash
            { 'action' : "pause",   'duration'  : .8 },
            { 'action' : "flash",   'duration'  : 2.2 },

            # 4 Crackles a bit and pauses
            { 'action' : "crackle", 'duration'  : .4 },
            { 'action' : "pause",   'duration'  : .6 },

            # 5 Tiny flash and then pauses
            { 'action' : "flash",   'duration'  : .2 },
            { 'action' : "pause",   'duration'  : .8 },

            # 6 Crackles a bit more briefly and then pauses
            { 'action' : "crackle",   'duration'  : .4 },
            { 'action' : "pause", 'duration'  : .6 },

            # 7 Tiny flash and then pauses
            { 'action' : "flash",   'duration'  : .1 },
            { 'action' : "pause",   'duration'  : .9 },

            # 8 Flickers a bit more briefly and then pauses
            { 'action' : "flicker",   'duration'  : .2 },
            { 'action' : "pause", 'duration'  : .6 },

        ]
    },
    {
        'description' :   "Starts with a boom and then flickers and fades.",
        'thunderFile' : "thunder-03.mp3",
        'lightningPattern'  :   [

            # 1 Hesitates for half a second and then flickers a bit
            { 'action' : "pause",   'duration'  : .5 },
            { 'action' : "flicker", 'duration'  : .5 },

            # 2 Builds to a crackle and pauses
            { 'action' : "flicker", 'duration'  : .25 },
            { 'action' : "crackle",   'duration'  : .5 },
            { 'action' : "flicker",   'duration'  : .25 },

            # 3 flicker pause flicker
            { 'action' : "pause",   'duration'  : .4 },
            { 'action' : "flicker",   'duration'  : .2 },
            { 'action' : "pause",   'duration'  : .2 },
            { 'action' : "flicker",   'duration'  : .2 },

            # 4 shorter flickers that fade out
            { 'action' : "pause",   'duration'  : .5 },
            { 'action' : "flicker",   'duration'  : .1 },
            { 'action' : "pause",   'duration'  : .3 },
            { 'action' : "flicker",   'duration'  : .1 },

            # 5 Barely anything, maybe a short flicker
            { 'action' : "pause",   'duration'  : .3 },
            { 'action' : "flicker",   'duration'  : .1 },
            { 'action' : "pause",   'duration'  : .6 },

            # 6. basically a long pause, maybe a tiny flash
            { 'action' : "crackle",   'duration'  : .2 },
            { 'action' : "pause", 'duration'  : .8 },

            # 6. basically a long pause, maybe a tiny flash
            { 'action' : "flash",   'duration'  : .3 },
            { 'action' : "pause", 'duration'  : .7 },



        ]
    },
]

# loop through each strike object

while True:
    for strike in strikes:

        secondsPassed = 0
        startTime = time.time()

        # play the sound file and trigger the relay according to the strike object's light pattern

        file = "Sounds/" + strike['thunderFile']
        print("playing thunder track: " + file)

        secondsPassed = time.time() - startTime

        print("seconds passed: " + str(round(secondsPassed,2)))

        print("flashing light pattern: " + strike['description'])

        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        for pattern in strike['lightningPattern']:
            if (pattern['action'] == "flash"):
                flash(pattern['duration'])
            elif (pattern['action'] == "crackle"):
                pulse(pattern['duration'], .5)
            elif (pattern['action'] == "flicker"):
                pulse(pattern['duration'], .2)
            else:
                pause(pattern['duration'])

        secondsPassed = time.time() - startTime
        print("seconds passed: " + str(round(secondsPassed,2)))

        thunderDuration = 10

        timeRemaining = thunderDuration - secondsPassed

        if(timeRemaining < thunderDuration):
            time.sleep(timeRemaining)

        pygame.mixer.music.stop()

        secondsPassed = 0

GPIO.cleanup()
