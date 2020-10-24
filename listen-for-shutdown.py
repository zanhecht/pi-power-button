#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	GPIO.wait_for_edge(3, GPIO.FALLING)
	start = time.time()
	GPIO.wait_for_edge(3, GPIO.RISING)
	elapsed = (time.time() - start)
	if elapsed > 0.1:
		subprocess.run(['shutdown', '-h', 'now'], shell=False)
