import time
def functie1(ant):
	ant = (ant)
	a = True
	while a:
		print(ant)
		ant += 1
		time.sleep(0.1)
		if int(ant) == "100":
			a = False
			exit
		else:
			continue
functie1(20)