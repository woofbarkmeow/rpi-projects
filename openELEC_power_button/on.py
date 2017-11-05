#!/usr/bin/python
import sys
sys.path.append('storage/.kodi/addons/python.RPi.GPIO/lib')
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib/')
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.HIGH)
