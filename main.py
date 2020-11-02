# Create a pomodoro timer
# 25 minutes per pomodoro + 5 minute break
# 4 pomodoros form a set, followed by 15-30 minute break

import time
import sys


def PomTimer(duration=1500):
    """Sets Duration of Pomodoro Timer"""
    global pomCounter
    pomDuration = duration
    while pomDuration:
        min, sec = divmod(pomDuration, 60)
        timer = f'{min:02d}:{sec:02d}'
        print(timer, end='\r')
        time.sleep(1)
        pomDuration -= 1
    pomCounter += 1
    print(f"Done!!! You have completed {pomCounter} Pomodoros!")


def BreakTimer(duration=300):
    """Sets Duration of Break Timer"""
    breakDur = duration
    while breakDur:
        min, sec = divmod(breakDur, 60)
        timer = f'{min:02d}:{sec:02d}'
        print(timer, end='\r')
        time.sleep(1)
        breakDur -= 1
    print("Your break is over!")


def GetDur():
    """Ask User for Input on Duration of Timers"""
    print("The")
    answerOne = input("Do you want to use preset timers? (y/n) \n")
    if answerOne.lower() not in ('y', 'n'):
        answerOne.lower()
        pass


def Help():
    """Provide User with Program Info"""
    while True:
        helpAns = input("""
Choose from the following:
Enter "1" for info on the Pomodoro Timer.
Enter "2" for info about the program and author.
Enter "3" to return to the menu.
        """)
        if helpAns not in ('1', '2', '3'):
            print("Invalid Input.")
            continue
        elif helpAns == '1':
            print("""The Pomodoro Timer is a study/work method to help with focus.
The intent is to work in 20-25 minute periods, followed by a 3-5
minute break. The break after the fifth Pomodoro should be longer;
20 to 25 minutes.
            """)
            continue
        elif helpAns == '2':
            print("""Hey! If you're reading this - thanks for trying out my program!
I decided to try my hand at making this program because I wanted a
Pomodoro Timer - on my computer - that didn't do anything more than
what it should. That meant no collection of personal info,
no sending info: just a simple timer with a built in tracker.

Hopefully you've been able to make use of this program in your own
work and studies.

Cheers,
Wil
            """)
        elif helpAns == '3':
            break


# first, create a simple timer loop (with input)
pomCounter = 0
while True:
    print("Current Pom: " + str(pomCounter+1))
    print("Poms until long break: " + str(5-pomCounter))
    answer = input("""Hit 'y' to start your next pomodoro.
'n' or 'q' to exit. 'h' for help.
    """)

    if answer.lower() not in ('y', 'n', 'q', 'h'):
        print("Invalid input.")
        sys.exit(1)
    elif answer.lower() == 'y':
        PomTimer(10)
        BreakTimer(10)
    elif answer.lower() == 'h':
        Help()
    elif answer.lower() in ('q', 'n'):
        print("Goodbye!")
        sys.exit(0)
