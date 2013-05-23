"""
Author: Brandon Carnell
Source File: Dustbowl.py
Last Modified By: Brandon Carnell
Date Last Modified: May 21st, 2013
Description: A text based adventure game based on a level from
	          Valve's 2007 Team Fortress 2 game
Revision History: N/A
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

#second path split
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
		   
	checkSecondPath(secondPath)


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
	print ('Hope this works')
	time.sleep(1)
	print ('will it work?')
	print
	time.sleep(1)
	
		
	if chosenSecondPath == "Go":
		secondPath1()
	else:
		secondPath2()
		


def firstPath1():
	print "You go up the stairs."	
	sourcePath = 'stairs'
	chooseSecondPath(sourcePath)
		
def firstPath2():
	print "you walk out into the gorge. you die."
	sourcePath = 'gorge'
	chooseSecondPath(sourcePath)
	
def firstPath3():
	print "you walk down the hallway. you win for some reason."
	sourcePath = 'hallway'
	chooseSecondPath(sourcePath)
	
def secondPath1():
	print "you chose path Go"

def secondPath2():
	print "you chose path Shed"


	
def main():
		
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		
		
		displayIntro()
		pathNumber = chooseFirstPath()
		checkFirstPath(pathNumber)
		

	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
