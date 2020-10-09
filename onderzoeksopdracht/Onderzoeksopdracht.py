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
check1 = False
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
	write("Alright calm down and think...", 0.1)
	time.sleep(1)
	write("Which one do I choose: 1, 2 or 3?", 0.1)
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
		loop1 = input("Restart? Yes/No\n")
		if loop1 == "Yes" or q2 == "yes":
			check1 = True
			loop1 = False
			continue
		if loop1 == "No" or q2 == "no":
			pass
		else:
			write("That's not a valid response you potato!", 0.04)
			continue
if q1 == "2":
	clear()
	time.sleep(1.5)
	write("You grab one of the bottles with your feet but drop it while carrying...", 0.06)
	play("break.mp3", 0.1)
	time.sleep(1.5)
	write("The bottles left shards of sharp glass on the floor, while you try to pick one up and succeed your foot gets cut...", 0.08)
	time.sleep(1.5)
	write("You throw The shard of glass on your lap and from there onto the side of the chair...", 0.08)
	time.sleep(2)
	write("You try to grab the glass with your hands...", 0.08)
	time.sleep(2)
	write("You manage to cut the rope around your hands with the glass you obtained...", 0.08)
	time.sleep(0.5)
	write("You slowly cut the rope aroud your legs and freely move them...", 0.08)
	time.sleep(1)
	clear()
	time.sleep(0.5)
	write("You walk towards the door in the room wondering what's on the other side...", 0.08)
	time.sleep(1)
	write("You slowly open the door...", 0.08)
	play("opening.mp3", 0.3)
	time.sleep(3)
	time.sleep(0.5)
	write("You find yourself at a set of stairs which follow to a door...", 0.08)
	time.sleep(1)
	clear()
	time.sleep(0.5)
	write("You are greeted by the bright and warming smile of the sun...", 0.08)
	time.sleep(2)
	write("You've never felt happier being greeted by the sun in this hot forsaken country...", 0.08)
	time.sleep(2)
	write("After you realize that you have regained your freedom you start running...", 0.06)
	time.sleep(1.5)
	write("There aren't many things going through your head...", 0.06)
	time.sleep(1.5)
	write("Where am I going? You ask yourself...", 0.08)
	time.sleep(2)
	write("You spot a road which you recognise...", 0.08)
	time.sleep(1)
	play("running.mp3", 0.3)
	write("This road leads you home!", 0.06)
	time.sleep(2)
	write("As you run over de road you can see nothing but suddenly over the horizon your house appears...", 0.08)
	time.sleep(2)
	write("There! There it is!", 0.06)
	time.sleep(0.5)
	write("As you near your house your excitement grows...", 0.1)
	time.sleep(1)
	write("Keep running! Keep Running!", 0.06)
	time.sleep(0.5)
	write("Almost there im coming 💣♓♍♒♋♏●📪 ❖♋■♏⬧⬧♋📪 ♋■■♏!", 0.06)
	time.sleep(1.5)
#Trippy effect <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	play("static.mp3", 0.1)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.25)
	clear()
	print("Im sorry...")
	time.sleep(0.3)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.4)
	clear()
	play("static.mp3", 0.1)
	print("Im sorry...")
	time.sleep(0.6)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.2)
	clear()
	play("static.mp3", 0.1)
	print("Im sorry...")
	time.sleep(0.3)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.09)
	clear()
	print("Im sorry...")
	time.sleep(0.08)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.07)
	clear()
	print("Im sorry")
	time.sleep(0.06)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.05)
	clear()
	print("Im sorry...")
	time.sleep(0.04)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.03)
	clear()
	print("Im sorry...")
	time.sleep(0.02)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.01)
	clear()
	play("static.mp3", 0.1)
	print("Im sorry")
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.2)
	clear()
	play("static.mp3", 0.1)
	print("Im sorry...")
	time.sleep(0.3)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.09)
	clear()
	print("Im sorry...")
	time.sleep(0.08)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.07)
	clear()
	print("Im sorry")
	time.sleep(0.06)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.05)
	clear()
	print("Im sorry...")
	time.sleep(0.04)
	clear()
	print("✋❍ ⬧□❒❒⍓📬📬📬")
	time.sleep(0.03)
	clear()
	print("Im sorry")
	time.sleep(0.5)
	clear()
	time.sleep(2)
	write("You gently open the door...", 0.1)
	play("opening.mp3", 0.3)
	time.sleep(3)
	clear()
	play("damage.mp3", 0.5)
	time.sleep(0.05)
	play("damage.mp3", 0.5)
	time.sleep(0.05)
	play("damage.mp3", 0.5)
	time.sleep(1)
	play("premonition.mp3", 0.5)
	write("What happend...", 0.2)
	time.sleep(2)
	write("They're... they're...", 0.2)
	time.sleep(0.5)
	write("Dead...", 0.4)
	time.sleep(2)
	write("Why would... Would... Anyone do this...", 0.1)
	time.sleep(2)
	write("Your mind is wiped...", 0.08)
	time.sleep(1)
	write("You can see your mother and father lumped over against the wall...", 0.08)
	time.sleep(2)
	write("You walk over and feel their pulse praying for their lives...", 0.08)
	time.sleep(1)
	write("Your fathers dead...", 0.1)
	time.sleep(1)
	write("Your mother is as well...", 0.1)
	time.sleep(1)
	write("Your sister is no where to be found...", 0.08)
	time.sleep(1)
	write("You run up to her room but she's not there...", 0.08)
	time.sleep(1)
	write("You check your parents room...", 0.08)
	time.sleep(1)
	clear()
	time.sleep(1)
	write("Shocked you wipe your mind of any thoughts...", 0.08)
	time.sleep(2)
	write("There is nothing left for me...", 0.08)
	time.sleep(1)
	write("Perhaps I should just flee...", 0.08)
	time.sleep(1)
	write("You look at the house which is left in shambles...", 0.08)
	time.sleep(2)
	write("Everything is broken...", 0.08)
	time.sleep(1)
	write("Just like I am right now...", 0.08)
	time.sleep(2)
	write("I should make a choice...", 0.06)
	time.sleep(1)
	write("I can salvage and check for any usefull stuff left", 0.08)
	time.sleep(1)
	write("Or I can flee right now, because they might be looking for me...", 0.08)
	time.sleep(
	
	
if q1 == "3":
	clear()
	time.sleep(1.5)
	write("As you desperatly try to wringle your hands out of the rope which tie them together you hurt yourself...", 0.06)
	time.sleep(1.5)
	write("You have been angered by the frustration of trying to free yourself of this rope...", 0.06)
	time.sleep(1)
	write("As your frustration grows, so does your agression...", 0.08)
	time.sleep(1)
	write("You start flicking your arms around which produces quite some noise...", 0.08)
	time.sleep(1)
	write("You free yourself from the rope and untie the rope around your legs and stand up to admire the room you're in...", 0.06)
	time.sleep(1)
	write("You walk to a set of stairs which you spot, but as you walk there you hear people shouting some stuff in a weird language...", 0.06)
	time.sleep(2)
	write("Standing in the open doorway you decide to move...", 0.06)
	time.sleep(2)
	write("This is bad you can hear them getting closer...", 0.06)
	time.sleep(1)
	write("The talking stopped, but there is still someone there you just know it...", 0.06)
	time.sleep(1.5)
	clear()
	time.sleep(1)
	play("keys.mp3", 0.3)
	write("You hear the rattling of the keys...", 0.06)
	time.sleep(1)
	write("This is bad I need to hide...", 0.06)
	time.sleep(0.5)
	write("You crawl under a desk desperate for a good hiding spot and desperate that he won't spot you...", 0.08)
	time.sleep(0.5)
	play("footsteps.mp3", 0.3)
	time.sleep(3)
	write("As you hear him walking down the stairs you just faced your heartbeat begins to speed up...", 0.06)
	play("heartbeat.mp3", 0.4)
	play("gun_cock.mp3", 0.4)
	time.sleep(1.5)
	write("If he finds you now its game over and you know it...", 0.08)
	time.sleep(1)
	write("As your high heartbeat continues you don't know what to do...", 0.08)
	time.sleep(1)
	write("He dissapeared from your sights and you don't see anything...", 0.08)
	play("gunshot.mp3", 0.4)
	time.sleep(2)
	write("Before you even can process what happend you see blood and feel a pain in your leg...", 0.08)
	time.sleep(1)
	write("There you are you scum!", 0.05)
	time.sleep(0.5)
	write("As the man who just fired his gun kicks the desk you are once again revealed to the room...", 0.08)
	time.sleep(1)
	play("gunshot.mp3", 0.4)
	write("As the man points his gun at you he right after pulls the trigger...", 0.1)
	time.sleep(1)
	write("You died...", 0.2)
	loop2 = True
	while loop2:
		loop2q = input("Restart? Yes/No\n")
		if loop2q == "Yes" or loop2q == "yes":
			break
			check1 = True
			continue
		if loop2q == "No" or loop2q == "no":
			break
		else:
			write("That's not a valid response you potato!", 0.04)
			continue


