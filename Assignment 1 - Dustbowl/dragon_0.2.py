import time

def displayIntro():
	print ('You are on a planet full of dragons. In front of you,')
	print ('you see two caves. In one cave, the dragon is friendly')
	print ('and will share his treasure with you. The other dragon')
	print ('is greedy and hungry, and will eat you on sight.')
	print
	
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2' and cave !='3':
		print ('Which cave will you go into? (1, 2 or 3)')
		cave = raw_input()
		if cave != '1' and cave != '2' and cave !='3':
		   print('I did not understand that.')
		   print
	return cave

def cave1():
	print "you've fit the first death"
def cave2():
	print "you've fit the second death"
def cave3():
	print "you win!"

		
def checkCave(chosenCave):
	print ('You approach the cave...')
	time.sleep(1)
	print ('It is dark and spooky...')
	time.sleep(1)
	print ('A large dragon jumps out in front of you! He opens his jaws and...')
	print
	time.sleep(1)
	
	
	if chosenCave == "1":
		cave1()
	elif chosenCave == "2":
		cave2()
	else:
		cave3()
		

def main():
		
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		caveNumber = chooseCave()
		checkCave(caveNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
