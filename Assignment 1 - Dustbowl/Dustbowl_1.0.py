"""
Author: Brandon Carnell
Source File: Dustbowl.py
Last Modified By: Brandon Carnell
Date Last Modified: May 23rd, 2013
Description: A text based adventure game based on a level from
	          Valve's 2007 Team Fortress 2 game
Revision History: Version 0.3
"""

import time

#This is the opening text. It will always be displayed first
#upon starting the program, or restarting after a failed ending.
def displayIntro():
	print ("Today you decide to play Team Fortress 2. Eventually you find your way onto Cp_Dustbowl, a popular map.")
	print ("You join the BLU team as a Scout, one of the weakest classes. While you will not survive long in teamfights,")
	print ("you do great in one-on-one situations and excel at capturing points.") 
	print ("You notice that your team isn't doing so well, so you go off to try and capture the point.")
	print #Empty Spacing
	time.sleep(1)
	print ("Leaving spawn you are stuck with the first of many decisions.") 
	print ("Do you go up the stairs, through the gorge, or down the hallway?")
	time.sleep(1)
	print #Empty Spacing

#Choose the first branch off. This is always after the opening,	
#and is the only branch that has three options
def chooseFirstPath():
	firstPath = ''
	while firstPath != 'stairs' and firstPath != 'gorge' and firstPath !='hallway':
		

		print ('Which path will you take? (stairs, gorge or hallway)')
		firstPath = raw_input().lower()
		
		if firstPath != 'stairs' and firstPath != 'gorge' and firstPath !='hallway':
		   print('I did not understand that.')
		   print #Empty Spacing
		   
	return firstPath

#Choose the second and onwards branches. It will decide what to display
#based off of which path you chose first.

#Second branches ( Stairs, Gorge, and Hallway)
def chooseSecondPath(sourcePath):
	secondPath = ''
	
	if sourcePath == "stairs":
		time.sleep(1)
		print ("Going up the stairs you see the enemy team pushing in on you.")
		print ("eventually both teams have there guns ablazing, with rockets, fire, and bullets going in every direction.")
		print ("Do you join the firefight or duck behind a shed nearby?")
		print #Empty Spacing
		
		while secondPath != 'go' and secondPath !='shed':
			print ("pick another path (go or shed)")
			secondPath = raw_input().lower()
			if secondPath != 'go' and secondPath != 'shed':
				print ('I did not understand that.')
		   		print #Empty Spacing
	
	if sourcePath == "gorge":
		time.sleep(1)
		print ("You decide to go through the gorge. While running through the low chasm when you here a crackling noise come from behind you.") 
		print ("You could look back to see what happened, or ignore it and run on ahead.")
		print #Empty Spacing
		
		while secondPath != 'back' and secondPath != 'run':
			print"pick another path (Back or Run)"
			secondPath = raw_input().lower()
			if secondPath !='back' and secondPath != 'run':
				print ('I did not understand that.')
		   		print #Empty Spacing
		   		
	if sourcePath == "hallway":
		time.sleep(1)
		print ("You decide to take the longer walk down the hallway. Your now outside, facing across the gorge.") 
		print ("Do you try to jump across it or sneak along the wall and go behind enemy lines?")
		print #Empty Spacing
		
		while secondPath != 'jump' and secondPath != 'sneak':
			print "pick another path (jump or sneak)"
			secondPath = raw_input().lower()
			if secondPath !='jump' and secondPath != 'sneak':
				print ('I did not understand that.')
		   		print #Empty Spacing
		
	checkSecondPath(secondPath)
	
	
#Third Branches (Go, Shed, Back, Run, Jump, and Sneak)
def chooseThirdPath(sourcePath):
	thirdPath = ''
	
	if sourcePath == "go":
		time.sleep(1)
		print ("You decide to keep going forward.") 
		print ("You somehow miraculously make it to the door of the control point without even getting shot at.") 
		print ("You could go through the door, but there is also a small window ledge you could jump up to.")
		print #Empty Spacing
		
		while thirdPath != 'door' and thirdPath !='ledge':
			print "pick another path (door or ledge)"
			thirdPath = raw_input().lower()
			if thirdPath != 'door' and thirdPath != 'ledge':
				print('I did not understand that.')
		   		print #Empty Spacing

	if sourcePath == "shed":
		time.sleep(1)
		print ("You decide to duck back behind the shed. You know that the enemy team is just up ahead,") 
		print ("so you figure that the rest of your team could deal with them first.") 
		print ("After a minute or two you think the coast is clear. you could run out, or stay hiding amongst the crates.")
		print #Empty Spacing
		
		while thirdPath != 'run' and thirdPath !='crates':
			print "pick another path (run or crates)"
			thirdPath = raw_input().lower()
			if thirdPath != 'run' and thirdPath != 'crates':
				print('I did not understand that.')
		   		print #Empty Spacing	
		   			   		
	if sourcePath == "back":
		time.sleep(1)
		print ("You take a second to see what that noise was. Before your eyes an enemy RED spy uncloaks his Dead Ringer.") 
		print ("You see he's holding his Knife, which will kill you instantly if he manages to strike you in the back.") 
		print ("You could fight the spy, but as a Scout you could easily ignore him and keep running.")
		print #Empty Spacing
		
		while thirdPath != 'fight' and thirdPath !='ignore':
			print "pick another path (fight or ignore)"
			thirdPath = raw_input().lower()
			if thirdPath != 'fight' and thirdPath != 'ignore':
				print('I did not understand that.')
		   		print #Empty Spacing
		   		
	if sourcePath == "run":
		time.sleep(1)
		print ("You decide to ignore the noise. Your a scout, you have places to cap and people to shoot,") 
		print ("petty distractions aren't going to bother you this time.")
		print ("After dodging through the enemies gunfire for while, you finally make it to the building your suppose to be capturing.") 
		print ("Before you walk into poorly built shack,")
		print ("you notice Sniper facing away from you. Do you take the opputunity to weaken there team, or stick to the task on hand?")
		print #Empty Spacing
		
		while thirdPath != 'sniper' and thirdPath !='task':
			print "pick another path (sniper or task)"
			thirdPath = raw_input().lower()
			if thirdPath != 'sniper' and thirdPath != 'task':
				print('I did not understand that.')
		   		print #Empty Spacing
		   		
	if sourcePath == "jump":
		time.sleep(1)
		print ("You make a daring leap across the chasm. your now behind most of the team, who were to busy to notice your lunge.")
		print ("You see an enemy Heavy under attack from the rest of your team.")
		print ("He looks to be almost defeated and is calling for a Medic to heal him back up to strength.") 
		print ("You could deal with him, or let your team finish him off and continue to the control point.")
		print #Empty Spacing
		
		while thirdPath != 'heavy' and thirdPath !='point':
			print "pick another path (heavy or point)"
			thirdPath = raw_input().lower()
			if thirdPath != 'heavy' and thirdPath != 'point':
				print('I did not understand that.')
		   		print #Empty Spacing
		   		
	if sourcePath == "sneak":
		time.sleep(1)
		print ("You sneak along the outermost walls of the dusty map.")
		print ("No one on either your own or the enemy team seems to have noticed you.") 
		print ("Coming from behind the enemy lines you see that a RED Engineer had prepared a Sentry Gun to face the doorway.") 
		print ("He runs off to go get more metal to upgrade it. Now is your chance to either take care of him, or his machine.")
		print #Empty Spacing
		
		while thirdPath != 'sentry' and thirdPath !='engie':
			print "pick another path (sentry or engie)"
			thirdPath = raw_input().lower()
			if thirdPath != 'sentry' and thirdPath != 'engie':
				print('I did not understand that.')
		   		print #Empty Spacing	
		   		
		   			   				   				   				   		
	checkThirdPath(thirdPath)
	
def chooseFourthPath(sourcePath):
	fourthPath = ''
	if sourcePath == "engie":
		
		time.sleep(1)
		print("You decide to follow the Engineer back towards the enemies base. As you get dangerously closer and closer, you choose to strike!")
		print("You can either use the weaker but faster Pistol, or the slower but powerful Scattergun.")
		
		while fourthPath != 'pistol' and fourthPath !='scattergun':
			print "pick another path (pistol or scattergun)"
			fourthPath = raw_input().lower()
			if fourthPath != 'pistol' and fourthPath != 'scattergun':
				print('I did not understand that.')
		   		print #Empty Spacing	
		   		
		   			   				   				   				   		
	checkFourthPath(fourthPath)
	
def chooseFinalPath(sourcePath):
	finalPath = ''
	if sourcePath == "scattergun":
		
		time.sleep(1)
		print("You take out your trusty Scattergun and fire off a shot.")
		print("The Engie is heavily damaged from that shot alone, and you finish him off with another.")
		print("Running back to the point, you hear the beeps of your former enemies Sentry.")
		print("You could cap the point now, or rub salt in the wound and fight the Sentry.")
		
	while finalPath != "ignore" and finalPath != "fight":
		print "pick another path (ignore or fight)"
		finalPath = raw_input().lower()
		if finalPath != 'ignore' and finalPath != 'fight':
			print('I did not understand that.')
		   	print #Empty Spacing
			
	checkFinalPath(finalPath)
	
	
#The first and second batches of paths only filter ahead.
#Starting at the third paths, game endings start appearing.

def checkFirstPath(chosenFirstPath):
		
	if chosenFirstPath == "stairs":
		firstPath1()
	elif chosenFirstPath == "gorge":
		firstPath2()
	else:
		firstPath3()
		
def checkSecondPath(chosenSecondPath):

	if chosenSecondPath == "go":
		secondPath1()
	elif chosenSecondPath == "shed":
		secondPath2()
	elif chosenSecondPath == "back":
		secondPath3()
	elif chosenSecondPath == "run":
		secondPath4()
	elif chosenSecondPath == "jump":
		secondPath5()
	else:
		secondPath6()

def checkThirdPath(chosenThirdPath):

	if chosenThirdPath == "door":
		time.sleep(1)
		print ("You run through the main door. within seconds the point starts to change to your teams colours.")
		print ("As you are capping though, the enemy team comes through the same door you did.")
		print ("It seems as though they defeated the rest of your team, and very quickly you are underfire from all kinds of weaponry.")
		print ("You do not survive the attack.")
		time.sleep(1)
		print ("GAME OVER")
		
	elif chosenThirdPath == "ledge":
		time.sleep(1)
		print ("You hop up onto the wooden ledge. Thinking the coast is clear, you step into the build from your unusual location.")
		print ("In less than a second, a Sentry Gun built by the enemy teams Engineer turns you into a splatter on the wall.")
		print ("Next time you'll think of a different tactic.")
		time.sleep(1)
		print ("GAME OVER")
		
	elif chosenThirdPath == "run":
		time.sleep(1)
		print ("You decide to run out, enough hiding for you.")
		print ("As you do though, you do not notice that a RED Demoman had left sticky bombs all over the shed!")
		print ("He saw you run back there, and watched from a distance.")
		print ("The last thing you hear is a small beep before being blasted into thin gruel")
		time.sleep(1)
		print ("GAME OVER")
		
	elif chosenThirdPath == "crates":
		time.sleep(1)
		print ("You decide to wait a little bit longer.")
		time.sleep(1)
		print ("Maybe too long, because as you make yourself at home behind the cover, the Annoucer declares the round ending countdown")
		print ("5,") 
		time.sleep(1)
		print ("4,") 
		time.sleep(1)
		print ("3,") 
		time.sleep(1)
		print ("2,") 
		time.sleep(1)
		print ("1,") 
		time.sleep(1)
		print ('"Failure!" she crys out. "You let your team down. Hopefully this will be a lesson to you."')
		time.sleep(1)
		print ("GAME OVER")
		
	elif chosenThirdPath == "fight":
		time.sleep(1)
		print ("You decide to take on your french speaking enemy with your trusty Scattergun.")
		print ("You get a few good shots on him, but start getting a little cocky.")
		print ("Upon getting to close to this espionage expert, he digs his knife right into your spine.")
		print ("Just as you expect, you die near instantly.")
		time.sleep(1)
		print ("GAME OVER")
		
	elif chosenThirdPath == "ignore":
		time.sleep(1)
		print ("You ignore the frenchman's taunting and booing. You can tell by the way he's dressed that that man knows his stuff,")
		print ("and the last thing you want today is a knife in your back. You continue up the minetrack covered path when without notice")
		print ("BANG")
		print ("An enemy sniper had been waiting to get a good shot on you, and you walk right into his sights.")
		time.sleep(1)
		print ("GAME OVER")
			
	elif chosenThirdPath == "sniper":
		time.sleep(1)
		print ("The point can wait, if you get rid of this Aussie maybe your teamates won't have as many holes in there skulls.")
		print ("You start peppering him down with Pistol fire while closing in on him,")
		print ("when suddenly a RED Pyro comes around the corner, fresh from a hidden teleporter.")
		print ("You don't even have time to react as he quickly turns you into charcoal.")
		time.sleep(1)
		print ("GAME OVER")
		
	elif chosenThirdPath == "task":
		time.sleep(1)
		print ("You don't have time to deal with the austrailan today, and instead waltz into the building.")
		print ("You go around a corner a little too sharp,") 
		print ("and don't notice the Sentry Gun turn around from its positioning by the window and start leaving bullets in your body.")
		time.sleep(1)
		print ("GAME OVER")
		
	elif chosenThirdPath == "heavy":
		time.sleep(1)
		print ("The once near undefeatable behemoth is now on his last leg.")
		print ("You start contributing to onslaught of damage the beast is taking.")
		print ("He see's you blasting away at you, and decides if he's going down, you are too.")
		print ("With his last ounce of health, he turns his massive Minigun around to you, blowing many small holes into you.")
		print ("As you see the beast fall down, you too collapse.")
		time.sleep(1)
		print ("GAME OVER")		
		
	elif chosenThirdPath == "point":
		time.sleep(1)
		print ("That Heavy's done like dinner with your team on him. You still have a point to capture.")
		print ("Walking through the doorway your met with an unexpected guest, the Medic the Heavy's been calling for!")
		print ("You hardly get a word out before he impales his Ubersaw into your abdomen.")
		print ("Normally you would've walked away from such an injury, but the doctor was lucky enough to score a critical,")
		print ("doing at least double the amount, easily enough to take you down in one shot.")
		time.sleep(1)
		print ("GAME OVER")
		
	elif chosenThirdPath == "sentry":
		time.sleep(1)
		print ("You run up to the mechanical device and start blasting it to smithereens.")
		print ("As you start capturing the point, a very angry looking RED Engineer comes back to what was his sentry")
		print ("In a fit of rage, he starts shooting down on you with his shotgun.")
		print ("Maybe next time you'll deal with the problem at the source.")
		time.sleep(1)
		print ("GAME OVER")
	else:
		thirdPath1()
		
def checkFourthPath(chosenFourthPath):
	if chosenFourthPath == "pistol":
		time.sleep(1)
		print("You whip out your Pistol and start your sneak attack. You manage to get a few shots on the Engie before he notices its you.")
		print("Unfortunately, you don't appear to do enough damage to take him down. He reaches for his Shotgun and riddles you back with buckshot.")
		print("You don't win this fight, at least, not this time.")
		time.sleep(1)
		print ("GAME OVER")
	else:
		finalPath()
		
def checkFinalPath(chosenFinalPath):
	if chosenFinalPath == "ignore":
		time.sleep(1)
		print("You decide to ignore the beeping robot in the corner and head straight to the point")
		print("You get about halfway when an RED Soldier rocket-jumps his way into the room, taking you by surprise.")
		print("You are no match for his rocket launcher and general bulkyness compared to your lanky physique")
		time.sleep(1)
		print ("GAME OVER")
		
	else:
		time.sleep(1)
		print("You duck around the corner where the Sentry is. Slowly chipping away at it with whats left of your scattergun ammo and pistol.")
		print("When the machine is finally in pieces, you jump onto the capture point. ")
		print("In a few seconds time, you see the hologram go from a scarlet RED to azure BLU.")
		print("Your team finally catches up to you, and you continue to push back the enemy...")
		time.sleep(2)
		print #Empty Spacing
		print("CONGRADULATIONS! YOU WON!")

def firstPath1():
	print "You go up the stairs."	
	sourcePath = 'stairs'
	chooseSecondPath(sourcePath)
		
def firstPath2():
	print "you walk out into the gorge."
	sourcePath = 'gorge'
	chooseSecondPath(sourcePath)
	
def firstPath3():
	print "you walk down the hallway."
	sourcePath = 'hallway'
	chooseSecondPath(sourcePath)
	

	
def secondPath1():
	sourcePath ="go"
	chooseThirdPath(sourcePath)
def secondPath2():
	sourcePath ="shed"
	chooseThirdPath(sourcePath)
def secondPath3():
	sourcePath ="back"
	chooseThirdPath(sourcePath)
def secondPath4():
	sourcePath ="run"
	chooseThirdPath(sourcePath)
def secondPath5():
	sourcePath ="jump"
	chooseThirdPath(sourcePath)
def secondPath6():
	sourcePath ="sneak"
	chooseThirdPath(sourcePath)
	
def thirdPath1():	
	sourcePath = "engie"
	chooseFourthPath(sourcePath)
	
def finalPath():
	sourcePath = "scattergun"
	chooseFinalPath(sourcePath)
	
def main():
		
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		
		displayIntro()
		pathNumber = chooseFirstPath()
		checkFirstPath(pathNumber)
		print #Empty Spacing
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input().lower()


if __name__ == "__main__": main()
