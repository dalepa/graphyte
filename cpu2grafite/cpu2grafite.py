#!/usr/bin/python
#encoding:utf-8

import os
import time
import graphyte
import statistics

from gpiozero import CPUTemperature

GRAPHITE="localhost"
graphyte.init(GRAPHITE, prefix='pi.cpu')


while True:
			
	cpu = CPUTemperature() 		
	graphyte.send('temp.fahrenheit',((cpu.temperature * (9/5)) + 32))
	print "temp = ", (cpu.temperature * (9/5)) + 32
	time.sleep(5)
	
