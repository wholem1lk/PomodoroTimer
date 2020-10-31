# Create a pomodoro timer
# 25 minutes per pomodoro + 5 minute break
# 4 pomodoros form a set, followed by 15-30 minute break

import time
import sys

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
        pomDuration = 10
        while pomDuration:
            min, sec = divmod(pomDuration, 60)
            timer = '{:02d}:{:02d}'.format(min, sec)
            print(timer, end="\r")
            time.sleep(1)
            pomDuration -= 1
        pomCounter += 1
        print(f"Times up!!! You have completed {pomCounter} Pomodoros!")
        breakDur = 5
        while breakDur:
            min, sec = divmod(breakDur, 60)
            brTimer = '{:01d}:{:01d}'.format(min, sec)
            print(brTimer, end='\r')
            time.sleep(1)
            breakDur -= 1
        print("Your break is over!")
    elif answer.lower() in ('q', 'n'):
        print("Goodbye!")
        sys.exit(0)
