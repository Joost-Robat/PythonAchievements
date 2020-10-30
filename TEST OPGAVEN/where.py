import random, time, 

people = ["Waldo","Henk","Mama","Wouter","Joost","Giel","Ruben","Jaro"]
nmr = 0
random.shuffle(people)

for naam in people:
	print(naam)
	nmr += 1
	if naam == "Waldo":
		print("Waldo is op nummer " + str(nmr))
		break
		