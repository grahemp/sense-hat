# sense-hat
This repository is some introductory work with my Raspberry Pi and the Sense Hat.
I started with downloading some files and doing some exploration from there.

I created a script that manipulates the LEDs and displays the time.  I use this for helping me to keep an eye on the time.  This is show-time.py
I run this through crontab every quarter hour.
0,15,30,45 * * * * /home/pi/sense-hat/python-sense-hat/show-time.py


