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
	print ("Today you decide to play Team Fortress 2. Eventually you find your way onto Cp_Dustbowl, a popular map. You join the BLU team as a Scout, one of the weakest classes. While you will not survive long in teamfights, you do great in one-on-one situations and excel at capturing points. You notice that your team isn't doing so well, so go off to try and capture the point.")
	print ("Leaving spawn you are stuck with the first of many decisions. Do you go up the stairs, through the gorge, or down the hallway?")


#Choose the first branch off. This is always after the opening,	
#and is the only branch that has three options
def chooseFirstPath():
	firstPath = ''
	while firstPath != 'stairs' and firstPath != 'gorge' and firstPath !='hallway':
		print ('Which path will you take? (stairs, gorge or hallway)')
		firstPath = raw_input()
		if firstPath != 'stairs' and firstPath != 'gorge' and firstPath !='hallway':
		   print('I did not understand that.')
		   print
		   
	return firstPath

#Choose the second and onwards branches. It will decide what to display
#based off of which path you chose first.

#Second branches
def chooseSecondPath(sourcePath):
	secondPath = ''
	
	if sourcePath == "stairs":
		print "Going up the stairs you see the enemy team pushing in on you. eventually both teams have there guns ablazing, with rockets, fire, and bullets going in every direction. Do you join the firefight or duck behind a shed nearby?"
		while secondPath != 'go' and secondPath !='shed':
			print "pick another path (go or shed)"
			secondPath = raw_input()
			if secondPath != 'go' and secondPath != 'shed':
				print('I did not understand that.')
		   		print
	
	if sourcePath == "gorge":
		print "You decide to go through the gorge. You start running through the low chasm when you here a crackling noise come from behind you. You could look back to see what happened, or ignore it and run on ahead."
		while secondPath != 'back' and secondPath != 'run':
			print"pick another path (Back or Run)"
			secondPath = raw_input()
			if secondPath !='back' and secondPath != 'run':
				print('I did not understand that.')
		   		print
		   		
	if sourcePath == "hallway":
		print "You decide to take the longer walk down the hallway. Your now outside, facing across the gorge. Do you try to jump across it or sneak along the wall and go behind enemy lines??"
		while secondPath != 'jump' and secondPath != 'sneak':
			print "pick another path (jump or sneak)"
			secondPath = raw_input()
			if secondPath !='jump' and secondPath != 'sneak':
				print('I did not understand that.')
		   		print
		
	checkSecondPath(secondPath)
	
	
#Third Branches
def chooseThirdPath(sourcePath):
	thirdPath = ''
	
	if sourcePath == "go":
		print "You decide to keep going forward. You somehow miraculously make it to the door of the control point without even getting shot at. You could go through the door, but there is also a small window ledge you could jump up to."
		while thirdPath != 'ONE' and thirdPath !='TWO':
			print "pick another path (ONE or TWO)"
			thirdPath = raw_input()
			if thirdPath != 'ONE' and thirdPath != 'TWO':
				print('I did not understand that.')
		   		print

	if sourcePath == "shed":
		print "You decide to duck back behind the shed. You know that the enemy team is just up ahead, so you figure that the rest of your team could deal with them first. After a minute or two you think the coast is clear. you could run out, or stay hiding amongst the crates."
		while thirdPath != 'ONE' and thirdPath !='TWO':
			print "pick another path (ONE or TWO)"
			thirdPath = raw_input()
			if thirdPath != 'ONE' and thirdPath != 'TWO':
				print('I did not understand that.')
		   		print	
		   			   		
	if sourcePath == "back":
		print "You take a second to see what that noise was. Before your eyes an enemy RED spy uncloaks his Dead Ringer. You see he's holding his Knife, which will kill you instantly if he manages to strike you in the back. You could fight the spy, but as a Scout you could easily ignore him and keep running."
		while thirdPath != 'ONE' and thirdPath !='TWO':
			print "pick another path (ONE or TWO)"
			thirdPath = raw_input()
			if thirdPath != 'ONE' and thirdPath != 'TWO':
				print('I did not understand that.')
		   		print
		   		
	if sourcePath == "run":
		print "You decide to ignore the noise. Your a scout, you have places to cap and people to shoot, petty distractions aren't going to bother you this time. After dodging through the enemies gunfire for while, you finally make it to the building your suppose to be capturing. Before you walk into poorly built shack, you notice Sniper facing away from you. Do you take the opputunity to weaken there team, or stick to the task on hand?"
		while thirdPath != 'ONE' and thirdPath !='TWO':
			print "pick another path (ONE or TWO)"
			thirdPath = raw_input()
			if thirdPath != 'ONE' and thirdPath != 'TWO':
				print('I did not understand that.')
		   		print
		   		
	if sourcePath == "jump":
		print "You make a daring leap across the chasm. your now behind most of the team, who were to busy to notice your lunge. You see an enemy Heavy under attack from the rest of your team. He looks to be almost defeated and is calling for a Medic to heal him back up to strength. You could deal with him, or let your team finish him off and continue to the control point."
		while thirdPath != 'ONE' and thirdPath !='TWO':
			print "pick another path (ONE or TWO)"
			thirdPath = raw_input()
			if thirdPath != 'ONE' and thirdPath != 'TWO':
				print('I did not understand that.')
		   		print
		   		
	if sourcePath == "sneak":
		print "You sneak along the outermost walls of the dusty map. No one on either your own or the enemy team seems to have noticed you. Coming from behind the enemy lines you see that a RED Engineer had prepared a Sentry Gun to face the doorway. He runs off to go get more metal to upgrade it. Now is your chance to either take care of him, or his machine."
		while thirdPath != 'ONE' and thirdPath !='TWO':
			print "pick another path (ONE or TWO)"
			thirdPath = raw_input()
			if thirdPath != 'ONE' and thirdPath != 'TWO':
				print('I did not understand that.')
		   		print	
		   		
		   			   				   				   				   		
	checkThirdPath(thirdPath)
	
	

#A small cinematic that splits into	the first three options	
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

	if chosenThirdPath == "":
		print"To be Added"
	


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
	print "you chose path Go"
	sourcePath ="Go"
	chooseThirdPath(sourcePath)
def secondPath2():
	print "you chose path Shed"
	sourcePath ="Shed"
	chooseThirdPath(sourcePath)
def secondPath3():
	print "you chose path Back"
	sourcePath ="Back"
	chooseThirdPath(sourcePath)
def secondPath4():
	print "you chose path Run"
	sourcePath ="Run"
	chooseThirdPath(sourcePath)
def secondPath5():
	print "you chose path Jump"
	sourcePath ="Jump"
	chooseThirdPath(sourcePath)
def secondPath6():
	print "you chose path Sneak"
	sourcePath ="Sneak"
	chooseThirdPath(sourcePath)
	
def main():
		
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		
		displayIntro()
		pathNumber = chooseFirstPath()
		checkFirstPath(pathNumber)

		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
