#uses Python 2.7.x

from grovepi import *
from grove_rgb_lcd import *
from time import *
from random import *
import threading


'''
DEPENDENCIES:
Grove Pi connections:
LCD screen into LCD port (middle port on USB/network input side)
LED light into D3
button into D4
Buzzer into D2

Text file named "scores.txt" in same folder as this file (error handling provided if file does not exist)
'''

# dictionary mapping colour codes to colour strings
colours = {"red": (255, 0, 0), "blue": (0, 102, 255), "green":(51, 204, 51), "yellow": (255, 255, 0), "orange": (255,165,0),
           "purple": (128,0,128)}

#some globals to communicate between functions
global running #a boolean to control the while loops
global r
global name

buzzer = 2
pinMode(buzzer, "OUTPUT")
led = 3
pinMode(led, "OUTPUT")
button = 4
pinMode(button, "INPUT")


def startGame(level, delay, lives, score):
    global name
    global r
    global running
    res=''
#    get a random colour name from dictionary
    x = choice(list(colours.keys()))
    while True:       
        inp = raw_input("You are on level " + str(level)+". Press the button when you see the colour "+x.upper()+" on the screen. Enter 'Y' when you are ready ").lower() 
#wait for user confirmation before starting game
        if inp.strip() == "y":
            break        
    running = True

    #start thread to cycle colours on LCD screen
    threading.Thread(target=spin, args=[delay]).start()
    
    while running:
        button_status=digitalRead(button)
        if button_status==1: #if the button is pressed
            running = False
            print("You clicked on " + r)
            
            if r == x: #user clicked on correct colour
                score+=1 #increment scrore
                res="Correct!"
                #turn light on
                digitalWrite(led,1)
                sleep(1) #leave light on
                digitalWrite(led,0) #turn light off
                if score%3==0:
                    level+=1  #bump up level and speed
                    delay*=.7
                    
            else: #user clicked on incorrect colour
                lives-=1 #subtract one life
                res="Wrong!"
                #turn buzzer on
                digitalWrite(buzzer,1)
                sleep(.2) #let buzzer buzz
                digitalWrite(buzzer,0) #turn buzzer off
            if lives == 0: #if no lives left, enter end routine
                print("")
                print("Game over. Your final score is "+ str(score) + ". You reached level "+str(level) + ". Thanks for playing")
                print("")
                f=open("scores.txt", "a")

                #write scores to file
                f.write(name+","+str(level)+","+str(score)+'\n') 
                f.close()
                printScores()
                running = False
            else:
                print(res +" Your score is "+ str(score) + ". You are on level "+str(level) + " with " + str(lives) + " lives remaining")
                startGame(level, delay, lives, score)   

def printScores():                
    print("\tHIGH SCORES TABLE")
    print(" =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    try:
        s=open("scores.txt", "r")
        print("Name\t\tLevel\t\tScore")
        print("-----\t\t-----\t\t-----")
        my_list=[]
        #open file, scan lines, make tuples, append to list
        for i in s:
            d=i.split(",")
            tup=(d[0],d[1],int(d[2].replace('\n', '')))
            my_list.append(tup)
        s.close()
        #sort results by score (3rd element in tuple), then reverse for descending order 
        my_list.sort(key=lambda x: x[2], reverse=True)
        for t in my_list:
            print(t[0]+"\t\t"+t[1]+"\t\t"+str(t[2]))
    except IOError:
        print("No high scores registered yet.")
        n = open("scores.txt", "w")
        n.close()
        
def spin(delay):
    global r
    global running
    while running:
        r= choice(list(colours.keys()))
        setRGB(colours[r][0], colours[r][1], colours[r][2])    
        sleep(delay)

#starting main process
print("")        
printScores()
print("")

#change this to input for python3
name=raw_input("Please enter your name: ")


#start thread to run main game (thread needed so we can run 2 while loops concurrently)
#args are level: 1, delay(speed): .7, lives: 3, score: 0

threading.Thread(target=startGame, args=[1, .7, 3, 0]).start()

