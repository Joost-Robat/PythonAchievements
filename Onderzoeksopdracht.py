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

check1 = True
while check1:
	write("You're in a land with no name...", 0.06)
	time.sleep(2.5)
	write("Who am I?", 0.1)
	time.sleep(0.5)
	write("Where am I?", 0.1)
	time.sleep(1.5)
	clear()
	write("Suddenly you remember...", 0.06)
	time.sleep(1.5)
	clear()
	write("You were walking back from work when you got hit on the back of your head...", 0.06)
	time.sleep(1.5)
	write("The land you're in is known for war...", 0.06)
	time.sleep(1.5)
	write("Only war...", 0.2)
	time.sleep(2)
	clear()
	time.sleep(2)
	write("You're blinded and can't see a thing...", 0.06)
	time.sleep(1.5)
	write("You should've made that deal with that smuggler...", 0.1)
	time.sleep(1.5)
	write("I need to find an escape...", 0.06)
	time.sleep(1.5)
	write("I've got limited choices but I have to work with what I have...", 0.06)
	time.sleep(2.5)
	clear()
	write("Your blindfold is loosely tied, and should come off easily...", 0.04)
	time.sleep(2)
	write("You shake your head furiously and the room is revealed while your blindfold slowly slides down...", 0.06)
	time.sleep(3)
	clear()
	write("There are three obvious choices that you can make right now...", 0.06)
	time.sleep(1.5)
	write("There's a C4 explosive in the room you're in...", 0.06)
	time.sleep(1)
	write("It's in kicking distance, but you don't know if it's been tempered with...", 0.06)
	time.sleep(1.5)
	write("There are a few bottles to your right, you don't know what they contain...", 0.08)
	time.sleep(1.5)
	write("Lastly there's the option to try and wringle your hands out the ropes that have tied them...", 0.06)
	time.sleep(2)
	write("Alright calm down and think...\nWich one do I choose: 1, 2 or 3?", 0.1)
	time.sleep(0.5)
	check1 = False
q1 = input()
if q1 == "1":
	clear()
	time.sleep(1)
	write("As you unleash your anger in a kick movement towards the C4 explosive it flies across the room against the wall", 0.04)
	time.sleep(3)
	write("Nothing happend...", 0.1)
	time.sleep(1)
	write("Alright to be honest I don't know what I was expe-", 0.04)
	write("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!!!!!", 0.01)
	write("The explosive flings you across the room against the wall leaving you injured with heavy bleeding wounds...", 0.08)
	time.sleep(2)
	write("You slowly lose sight and bleed out...", 0.15)
	time.sleep(1)
	write("You died...", 0.2)
	loop1 = True
	while loop1:
		q2 = input("Restart? Yes/No\n")
		if q2 == "Yes" or q2 == "yes":
			check1 = True
			continue
		if q2 == "No" or q2 == "no":
			pass
		else:
			write("That's not a valid response you potato!", 0.06)
			continue
if q1 == "2":
	clear()
	time.sleep(1.5)
	write("You grab one of the bottles with your feet but drop it while carrying...", 0.06)
	time.sleep(1.5)
	write("The bottles left shards of sharp glass on the floor, while you try to pick one up and succeed your foot gets cut...", 0.08)
	time.sleep(1.5)
	write("You throw The shard of glass on your lap and from there onto the side of the chair where you manage to grab it with your hand...", 0.08)
	time.sleep(2)
	write("You manage to cut the rope around your hands...", 0.08)
	time.sleep(0.5)
	write("You slowly cut the rope aroud your legs and freely move them...", 0.08)
	time.sleep(1)
	clear()
	time.sleep(0.5)
	write("You walk towards the door in the room wondering what's on the other side...", 0.08)
	time.sleep(1)
	write("You slowly open the door...", 0.06)
	time.sleep(0.5)
	write("You find yourself at a set of stairs wich follow to a door...", 0.06)
	time.sleep(1)
	clear()
	time.sleep(0.5)
	write("You are greeted by the birght and warming smile of the sun...", 0.06)
	time.sleep(2)
	write("You've never felt happier being greeted by the sun in this hot forsaken country...", 0.06)
	time.sleep(2)
	
if q1 == "3":
	clear
	time.sleep(1.5)
	write("As you desperatly try to wringle your hands out of the rope wich tie them together you hurt yourself...", 0.06)
	time.sleep(1.5)
	write("You have been angered by the frustration of trying to free yourself of this rope...", 0.06)
	time.sleep(1)
	write("As your frustration grows, so does your agression... You start flicking your arms around wich produces quite some noise...", 0.08)
	time.sleep(1)
	write("You free yourself from the rope and untie the rope around your legs and stand up admire the room you're in...", 0.06)
	time.sleep(1)




