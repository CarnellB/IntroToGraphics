import pygame
import random
import gameEngine
pygame.init()
"""
Source File Name: SuperNova.py
Last Modified by: Brandon C
Date Last Modified: August 15th 2013

Description: A simple sidescrolling game set in space,
             avoid asteroids and collect gems
             
Revision History: SuperNova_0.1 - player sprite added
                  SuperNova_0.2 - gem sprite added
                  SuperNova_0.3 - rock sprite added
                  SuperNova_0.4 - parralax background added
                  SuperNova_0.5 - music added
                  SuperNova_0.6 - collisions and multiple enemies added
                  SuperNova_0.7 - scoring and internal documentation added
                  SuperNova_0.8 - intro screen added
                  SuperNova_1.0 - project version; added animation
                 
"""

screen = pygame.display.set_mode((640, 480))

if not pygame.mixer:
    print("problem with sound")
else:
    pygame.mixer.init()
    sndBGM = pygame.mixer.Sound("BGM.ogg")
    sndHit = pygame.mixer.Sound("Hit.ogg")
    sndGem = pygame.mixer.Sound("Gem.ogg")
    
            
#The playable class, able to move upwards and downwards    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Player.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
       
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        if mousey < 15:
            mousey = 15
        if mousey > 465:
            mousey = 465
            
        if mousex < 15:
            mousex = 15
        if mousex > 625:
            mousex = 625
        self.rect.center = (mousex, mousey)

#The collectable class that increases your score        
class Gem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        
        self.frame = 0
        self.delay = 5
        self.pause = 0

        self.image = self.imgList[0]
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
        
    def update(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
            self.image = self.imgList[self.frame]        
        
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.left = screen.get_width() * 2
        self.rect.centery = random.randrange(16, screen.get_height() - 16)
        
    def loadImages(self):
        imgMaster = pygame.image.load("GemSheet.png")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (32, 32)
        offset = ((0, 0), (36, 0), (69, 0), (102, 0))

        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)

#The enemy class, hitting it with your ship too many times will end the game        
class BigRock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("BigRock.gif")
        
        
        self.loadImages()
        
        self.frame = 0
        self.delay = 5
        self.pause = 0

        self.image = self.imgList[0]
        self.rect = self.image.get_rect()
     
        self.reset()
    def loadImages(self):
        imgMaster = pygame.image.load("RockSheet.png")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (64, 64)
        offset = ((4,4), (76,4), (148,4), (220,4), (292,4), (364,4))
        
        for i in range(6):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)    

    def update(self):
        self.pause += 1
        if self.pause >= self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
                
            self.image = self.imgList[self.frame]
            
        self.rect.centerx -= self.dx
        self.rect.centery -= self.dy
        if self.rect.right < 0:
            self.reset()
       
    
    def reset(self):
        self.rect.left = screen.get_width() + 150
        self.rect.centery = random.randrange(25, screen.get_height() - 25)
        self.dy = random.randrange(-1, 1)
        self.dx = random.randrange(4, 12)
        
#The parralax scrolling background       
class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Space.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 2
        self.reset()
        
    def update(self):
        self.rect.left -= self.dx
        if self.rect.right <= screen.get_width():
            self.reset() 
    

    def reset(self):
        self.rect.left = 0

#The scoreboard, Goes up by 100 per gem, and 10 per second alive
class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.level = 0
        self.font = pygame.font.SysFont("Arial", 30)
        
        
    def update(self):
        self.text = "LIVES: %d, SCORE: %d, LEVEL: %d" % (self.lives, self.score, self.level)
        self.image = self.font.render(self.text, 1, (255, 215, 0))
        self.rect = self.image.get_rect()
        self.rect.right = screen.get_width() - 50
        if self.score > 200:
            self.level = 2 
        
class Title(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Title.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = screen.get_width() / 2
        
        
def game():
    pygame.display.set_caption("SuperNova Version 1.0")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # variables used to track how much time has gone by
    lastFrameTicks = pygame.time.get_ticks()
    scoreIncrementTimer = 0
    bonus = 100
    sndBGM.play(-1)
    
    player = Player()
    gem = Gem()
    score = Score()
    score.level += 1
    
    space = Space()
    
    
    gems = pygame.sprite.Group()
    gems.add(gem)

    #controls the number of asteroids appear on screen
    number_of_rocks = 5
    rocks_to_add = 0
    rocks = pygame.sprite.Group()
    for i in range(number_of_rocks):
        rock = BigRock()
        rocks.add(rock)

      
    allSprites = pygame.sprite.OrderedUpdates(space,score,gem,player,rocks)
    clock = pygame.time.Clock()
    adding_rocks = False
    keepGoing = True
    while keepGoing:
        print rocks.__len__()
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
         
        if score.level == 2:
            bonus = 150
            adding_rocks = True
            rocks_to_add = 5

        if adding_rocks == True:
            for i in range(rocks_to_add):
                rock = BigRock()
                rocks.add(rock)
                rocks.clear(screen, background)
                rocks.update()
                rocks.draw(screen)
        rocks_to_add = 0
        """
        Delta timer retrieved from
        http://stackoverflow.com/questions/10340550/pygame-simple-score-system 
        """
        thisFrameTicks = pygame.time.get_ticks()
        ticksSinceLastFrame = thisFrameTicks - lastFrameTicks
        lastFrameTicks = thisFrameTicks
     
        scoreIncrementTimer = scoreIncrementTimer + ticksSinceLastFrame
        if scoreIncrementTimer > 1000:
            score.score += 10
            scoreIncrementTimer = 0
      
        #If you collide with a gem, add 100 points to the score        
        hit = pygame.sprite.spritecollideany(player, gems, False)
        if hit != None:
            sndGem.play()
            score.score += bonus
            hit.reset()
            
        #if you collide with a rock, lose a life
        rock_hit_list = pygame.sprite.spritecollide(player, rocks, False)
        for rock in rock_hit_list:
            rock.reset() 
            score.lives -= 1
            sndHit.play()
            if score.lives <= 0:
                keepGoing = False
          
          
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    pygame.mouse.set_visible(True)
    sndBGM.stop()
    return score.score

#A small splash screen before the game starts up
def splash():
      pygame.display.set_caption("SuperNova Version 1.0")
      background = pygame.Surface(screen.get_size())
      background.fill((0, 0, 0))
      screen.blit(background, (0, 0))
      image = pygame.image.load("Splash.png")
      image = image.convert()
      screen.blit(image,(0,0))
      pygame.display.flip()
      pygame.time.delay(1000)

# An instruction screen to explain the game both before and after games
def instructions(score):
    pygame.display.set_caption("SuperNova Version 1.0")
    
    title = Title()
    player = Player()
    space = Space()
    

    
    allSprites = pygame.sprite.OrderedUpdates(space,player,title)
    insFont = pygame.font.SysFont("Arial",30)
    insLabels = []
    instructions = (
    "",
    "",
    "Last Score: %d" % score ,
    "Instructions:  Avoid the asteroids,",
    "collect the red gems for more score",
    "",
    "Grabbing the gems gives you bonus",
    "points. Points increase naturaly",    
    "over time. If you are hit by five",
    "asteroids your ship will fall apart!",
    "",
    "good luck!",
    "",
    "click anywhere to start,",
    "press Q to quit."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 215, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    keepGoing = False
                    donePlaying = True
    
        allSprites.update()
        allSprites.draw(screen)

        
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (150, 25*i))

        pygame.display.flip()
        
    sndBGM.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying

def main():
    
    donePlaying = False
    score = 0
    
    while not donePlaying:
        
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()
if __name__ == "__main__":
    splash()
    main()
            
