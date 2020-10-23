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
	if elapsed > 3:
		subprocess.run(['shutdown', '-h', 'now'], shell=False)
	elif elapsed > 0.1:
		status=subprocess.run(['uhubctl', '-l',  '1-1', '-p', '1'], capture_output=True).stdout.splitlines()[-1].split()[3]
		cmd = 'off' if status==b'power' else 'on'
		subprocess.run(['uhubctl', '-a', cmd, '-l', '1-1'])
