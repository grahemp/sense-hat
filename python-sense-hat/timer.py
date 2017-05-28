#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0]
R = [255, 0, 0]
B = [0, 0 ,255]
X = [ 0,0,0]

# number of interations
s = 25
interval = 60  # how many seconds.

timer = []

sense.clear

for i in range(64):
  if i < s:
    timer.append(G)
  else:
    timer.append(X)
    
for i in range(1, 10):
 sense.clear
 sleep(0.1)
 sense.set_pixels(timer)
 sleep(0.1)

sense.set_pixels(timer)

for i in range(0, s):
  sleep(1)
  timer[i] = B
  sense.set_pixels(timer)
  
for i in range(1, 10):
 sense.clear
 sleep(0.1)
 sense.set_pixels(timer)
 sleep(0.1)

sense.clear


X = [0, 0, 0]

gtimer = []
rtimer = []
btimer = []
xtimer = []

for i in range(64):
    gtimer.append(G)

for i in range(64):
    rtimer.append(R)

for i in range(64):
    btimer.append(B)

for i in range(64):
    xtimer.append(X)

for i in range(10):
	sense.clear
	sense.set_pixels(gtimer)
	sleep(0.2)
	sense.clear
	sense.set_pixels(rtimer)
	sleep(0.2)
	sense.set_pixels(btimer)
	sleep(0.2)
	sense.set_pixels(xtimer)
	sleep(0.1)
	sense.clear

