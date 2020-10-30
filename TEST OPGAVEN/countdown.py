import time
a = True
nmr = 10
while a:
	time.sleep(1)
	nmr -= 1
	print(nmr)
	if nmr == 0:
		print("I just took a 1000 secons of your time and your never getting them back!")
		break