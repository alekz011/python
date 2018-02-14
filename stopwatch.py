#! /usr/bin/python3

import time

# Display the program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. PRess CTRL+C to quit')

input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap time

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum +=1
        lastTime = time.time()

except KeyboardInterrupt:
    print('\nDone')
