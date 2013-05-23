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
	print ('A opening will be put here in a later version')
	print


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
def chooseSecondPath(sourcePath):
	secondPath = ''
	
	if sourcePath == "stairs":
		print "You see a shed, do you hide behind it or go on ahead?"
		while secondPath != 'Go' and secondPath !='Shed':
			print "pick another path (Go or Shed)"
			secondPath = raw_input()
			if secondPath != 'Go' and secondPath != 'Shed':
				print('I did not understand that.')
		   		print
	
	if sourcePath == "gorge":
		print "You hear a noise from behind you. do you look back or run ahead?"
		while secondPath != 'Back' and secondPath != 'Run':
			print"pick another path (Back or Run)"
			secondPath = raw_input()
			if secondPath !='Back' and secondPath != 'Run':
				print('I did not understand that.')
		   		print
		   		
	if sourcePath == "hallway":
		print "You come flying out of the hallway. Your now above the gorge. Do you try to jump across it or sneak along the wall?"
		while secondPath != 'Jump' and secondPath != 'Sneak':
			print "pick another path (Jump or Sneak)"
			secondPath = raw_input()
			if secondPath !='Jump' and secondPath != 'Sneak':
				print('I did not understand that.')
		   		print
		
		   
	checkSecondPath(secondPath)

def chooseThirdPath(sourcePath):
	thirdPath = ''
	
	if sourcePath == "stairs":
		print "You see a shed, do you hide behind it or go on ahead?"
		while thirdPath != 'Go' and thirdPath !='Shed':
			print "pick another path (Go or Shed)"
			thirdPath = raw_input()
			if thirdPath != 'Go' and thirdPath != 'Shed':
				print('I did not understand that.')
		   		print
	
	if sourcePath == "gorge":
		print "You hear a noise from behind you. do you look back or run ahead?"
		while thirdPath != 'Back' and thirdPath != 'Run':
			print"pick another path (Back or Run)"
			thirdPath = raw_input()
			if thirdPath !='Back' and thirdPath != 'Run':
				print('I did not understand that.')
		   		print
		   		
	if sourcePath == "hallway":
		print "You come flying out of the hallway. Your now above the gorge. Do you try to jump across it or sneak along the wall?"
		while thirdPath != 'Jump' and thirdPath != 'Sneak':
			print "pick another path (Jump or Sneak)"
			thirdPath = raw_input()
			if thirdPath !='Jump' and thirdPath != 'Sneak':
				print('I did not understand that.')
		   		print
		
		   
	checkThirdPath(thirdPath)
	
	

#A small cinematic that splits into	the first three options	
def checkFirstPath(chosenFirstPath):
	print ('You stand around for a short period.')
	time.sleep(1)
	print ('getting bored, you decide to leave the spawn area.')
	print
	time.sleep(1)
	
		
	if chosenFirstPath == "stairs":
		firstPath1()
	elif chosenFirstPath == "gorge":
		firstPath2()
	else:
		firstPath3()
		
def checkSecondPath(chosenSecondPath):

	if chosenSecondPath == "Go":
		secondPath1()
	elif chosenSecondPath == "Shed":
		secondPath2()
	elif chosenSecondPath == "Back":
		secondPath3()
	elif chosenSecondPath == "Run":
		secondPath4()
	elif chosenSecondPath == "Jump":
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
