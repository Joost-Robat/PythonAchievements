import time
from time import sleep
import sys
import os
clear = lambda: os.system('cls')
clear()
from pygame._sdl2 import *
from pygame import mixer

mixer.init(devicename='Oortelefoon van hoofdtelefoon (HyperX Virtual Surround Sound)') #run de audio.py in cmd voor uw huidige audiodevice

def play(mp3, volume):
	sound = mixer.Sound(mp3)
	sound.play()
	sound.set_volume(volume)

def write(text, speed):
	for x in text:
		print(x, end='')
		sys.stdout.flush()
		sound = mixer.Sound("blop.mp3")
		sound.play()
		sound.set_volume(0.7)
		sleep(speed)
	print("\n")
clear()
check1 = True
while check1:
	play("1.mp3", 0.5)
	write("You're in a land with no name...", 0.06)
	time.sleep(2.5)
	write("Who am I?", 0.1)
	time.sleep(0.5)
	write("Where am I?", 0.1)
	time.sleep(1.5)
	clear()
	time.sleep(0.5)
	write("Suddenly you remember...", 0.06)
	time.sleep(1.5)
	write("Your name is:\n", 0.08)
	name = input()
	time.sleep(1)
	write("That's right your name is " + name + "...", 0.08)
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
	write("As you unleash your anger in a kick movement towards the C4 explosive it flies across the room against the wall", 0.06)
	time.sleep(3)
	write("Nothing happend...", 0.1)
	time.sleep(2)
	write("Alright to be honest I don't know what I was expe-", 0.04)
	write("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!!!!!", 0.01)
	time.sleep(0.5)
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
			loop1 = False
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
	play("break.mp3", 0.1)
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
	write("You are greeted by the bright and warming smile of the sun...", 0.06)
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
	write("You walk to a set of stairs wich you spot, but as you walk there you hear people shouting some stuff in a weird language...", 0.06)
	time.sleep(2)
	write("This is bad you can hear them getting closer...", 0.06)
	time.sleep(1)
	write("The talking stopped, but there is still someone there you just know it...", 0.06)
	time.sleep(1)
	write("You hear the rattling of the keys...", 0.06)
	play("keys.mp3", 0.3)
	time.sleep(1)
	write("This is bad I need to hide..." 0.06)
	time.sleep(0.5)
	write("You crawl under a desk desperate for a good hiding spot and desperate that he won't spot you...", 0.06)
	time.sleep(0.5)
	play("footsteps.mp3", 0.3)
	time.sleep(3)
	write("As you hear him walking down the stairs you just faced your heartbeat begins to speed up...", 0.06)
	



