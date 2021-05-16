import pygame, time

pygame.init()

strikes = [
    {
        'thunder' : "thunder-01.mp3",
        'lightning' :   "pattern 1"
    },
    {
        'thunder' : "thunder-02.mp3",
        'lightning' :   "pattern 2"
    },
    {
        'thunder' : "thunder-03.mp3",
        'lightning' :   "pattern 3"
    },
    {
        'thunder' : "thunder-04.mp3",
        'lightning' :   "pattern 4"
    },
    {
        'thunder' : "thunder-05.mp3",
        'lightning' :   "pattern 5"
    },
    {
        'thunder' : "thunder-06.mp3",
        'lightning' :   "pattern 6"
    },
    {
        'thunder' : "thunder-07.mp3",
        'lightning' :   "pattern 7"
    },
    {
        'thunder' : "thunder-08.mp3",
        'lightning' :   "pattern 8"
    },
    {
        'thunder' : "thunder-09.mp3",
        'lightning' :   "pattern 9"
    },

]

while True:
    for strike in strikes:
        print("playing thunder track: " + strike['thunder'])
        print("flashing light pattern: " + strike['lightning'])
        #playsound("Sounds/" + strike['thunder'])
        pygame.mixer.music.load("Sounds/" + strike['thunder'])
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.stop()
