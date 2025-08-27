import time
import math
name = input ("What is your name? ")
age = int(input("How old are you? "))
food = input ("What is your faviorate food? ")
wpasstime = input ("What is your faviorate hobby? ")
lpasstime = input ("What is your least faviorate hobby? ")

print (f"Hi {name} .... thats a stupid name")
if age > 11:
    print (f"You're {age} and still eating {food} like a {age-11} year old")
else:
    print (f"Lil bro is {age}, not even 11 yet and already likes {food} XD")
race = input ("What race are you? ")
print ("Race is a low bar I'm not gonna say anything about that")
print (f"I heard you like to {wpasstime}, yea, that makes sense, youre a lazy bum who cant even do some {lpasstime}")
think = input ("What do you have to say about that? ")
print(1)
print (""" 
  _____       _             _                    _ _                            
 |_   _|     | |           | |                  | | |                           
   | |     __| | ___  _ __ | |_   _ __ ___  __ _| | |_   _    ___ __ _ _ __ ___ 
   | |    / _` |/ _ \| '_ \| __| | '__/ _ \/ _` | | | | | |  / __/ _` | '__/ _ |
  _| |_  | (_| | (_) | | | | |_  | | |  __/ (_| | | | |_| | | (_| (_| | | |  __/
 |_____|  \__,_|\___/|_| |_|\__| |_|  \___|\__,_|_|_|\__, |  \___\__,_|_|  \___|
                                                      __/ |                     
                                                     |___/                      
""")
def wait ():
    print ("...")
    time.sleep (3)
pass
wait()
wait()
wait()
wait()
wait()
bands = 0
finish = 0
while finish == 0:
    bands = input ("Do you have more than 10 bands  Y/N ")
    if bands == "Y":
        print ("Dont lie to me")
    elif bands == "N":
        print ("Broke XD")
        finish = 1
    else:
        print ("Y/N")
