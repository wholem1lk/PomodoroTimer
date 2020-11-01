# Create a pomodoro timer
# 25 minutes per pomodoro + 5 minute break
# 4 pomodoros form a set, followed by 15-30 minute break

import time
import sys


def PomTimer(duration=1500):
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
    breakDur = duration
    while breakDur:
        min, sec = divmod(breakDur, 60)
        timer = f'{min:02d}:{sec:02d}'
        print(timer, end='\r')
        time.sleep(1)
        breakDur -= 1
    print("Your break is over!")


# first, create a simple timer loop (with input)
pomCounter = 0
while True:
    print("Current Pom: " + str(pomCounter+1))
    print("Poms until long break: " + str(5-pomCounter))
    answer = input("Hit 'y' to start your next pomodoro. 'n' or 'q' to exit.")

    if answer.lower() not in ('y', 'n', 'q'):
        print("Invalid input.")
        sys.exit(1)
    elif answer.lower() == 'y':
        PomTimer(10)
        BreakTimer(10)
    elif answer.lower() in ('q', 'n'):
        print("Goodbye!")
        sys.exit(0)
