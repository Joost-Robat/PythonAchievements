import time
from time import sleep
import sys
import os
clear = lambda: os.system('cls')
clear()

def write(text, speed):
	for x in text:
		print(x, end='')
		sys.stdout.flush()
		sleep(speed)
	print("\n")

write("Michael is cool", 0.04)