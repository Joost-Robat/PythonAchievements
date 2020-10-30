a = True
import math
print("Rekemachine van Joost Robat Version 2.1")
while a:
	print("1.Keer\n2.Delen\n3.Optellen\n4.Aftrekken")
	q1 = input("(voer een nummer in)\n")
	if q1 == "1":
		g1 = input("? X ?\n")
		g2 = input(g1 + "X ?\n")
		ant = int(g1) * int(g2)
		print(ant)
		continue
	if q1 == "2":
		g1 = input("? / ?\n")
		g2 = input(g1 + "/ ?\n")
		ant = int(g1) / int(g2)
		print(ant)
		continue
	if q1 == "3":
		g1 = input("? + ?\n")
		g2 = input(g1 + "+ ?\n")
		ant = int(g1) + int(g2)
		print(ant)
		continue
	if q1 == "4":
		g1 = input("? - ?\n")
		g2 = input(g1 + "- ?\n")
		ant = int(g1) - int(g2)
		print(ant)
		continue
	else:
		print("Incorrecte invoer, probeer het nog een keer")
		continue