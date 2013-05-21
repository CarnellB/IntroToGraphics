#Author: Brandon Carnell
#Source File: Dustbowl.py
#Last Modified By: Brandon Carnell
#Date Last Modified: May 21st, 2013
#Description: A text based adventure game based on a level from
#	          Valve's 2007 Team Fortress 2 game
#Revision History: N/A

import time

def displayIntro():
	print ('A opening will be put here in a later version')
	print
	
def choosePath():
	firstPath = ''
	while firstPath != 'stairs' and firstPath != 'gorge' and firstPath !='hallway':
		print ('Which path will you take? (stairs, gorge or hallway)')
		firstPath = raw_input()
		if firstPath != 'stairs' and firstPath != 'gorge' and firstPath !='hallway':
		   print('I did not understand that.')
		   print
	return firstPath

def firstPath1():
	print "you go up the stairs. you die."
def firstPath2():
	print "you walk out into the gorge. you die."
def firstPath3():
	print "you walk down the hallway. you win for some reason."

		
def checkPath(chosenPath):
	print ('You stand around for a short period.')
	time.sleep(1)
	print ('getting bored, you decide to leave the spawn area.')
	print
	time.sleep(1)
	
	
	if chosenPath == "stairs":
		firstPath1()
	elif chosenPath == "gorge":
		firstPath2()
	else:
		firstPath3()
		

def main():
		
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		pathNumber = choosePath()
		checkPath(pathNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
