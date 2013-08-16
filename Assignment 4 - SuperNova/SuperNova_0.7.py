import pygame
import random
pygame.init()
"""
Source File Name: SuperNova_0.7.py
Last Modified by: Brandon C
Date Last Modified: July 15th 2013

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
"""

screen = pygame.display.set_mode((640, 480))

#The playable class, able to move upwards and downwards    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Player.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
          print("problem with sound")
        else:
          pygame.mixer.init()
          self.sndBGM = pygame.mixer.Sound("BGM.ogg")
          self.sndHit = pygame.mixer.Sound("Hit.ogg")
          self.sndGem = pygame.mixer.Sound("Gem.ogg")
          
          
          self.sndBGM.play(-1)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        if mousey < 15:
            mousey = 15
        if mousey > 465:
            mousey = 465
        self.rect.center = (45, mousey)

#The collectable class that increases your score        
class Gem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Gem.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
        
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
            
    def reset(self):
        self.rect.left = screen.get_width()
        self.rect.centery = random.randrange(16, screen.get_height() - 16)

#The enemy class, hitting it with your ship too many times will end the game        
class BigRock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("BigRock.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centerx -= self.dx
        self.rect.centery -= self.dy
        if self.rect.right < 0:
            self.reset()
       
    
    def reset(self):
        self.rect.left = screen.get_width()
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
        self.font = pygame.font.SysFont("Arial", 30)
        
        
    def update(self):
        self.text = "LIVES: %d, SCORE: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 215, 0))
        self.rect = self.image.get_rect()
        self.rect.right = screen.get_width() - 50
        
        
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("SuperNova Version 0.7")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # variables used to track how much time has gone by
    lastFrameTicks = pygame.time.get_ticks()
    scoreIncrementTimer = 0
    enemyTimer = 0
    
    player = Player()
    gem = Gem()
    score = Score()
    space = Space()

    #controls the number of asteroids appear on screen
    number_of_rocks = 6
    rocks = pygame.sprite.Group()
    for i in range(number_of_rocks):
      rock = BigRock()
      rocks.add(rock)
      
    allSprites = pygame.sprite.OrderedUpdates(space,score,gem,player,rocks)
    clock = pygame.time.Clock()
    
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
         
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
                
        #Code meant to add another rock enemy after 10 seconds, doesn't work
        """
        enemyTimer = enemyTimer + ticksSinceLastFrame
        if enemyTimer > 10000:
          number_of_rocks += 1
          rocks.add(rock)
          enemyTimer = 0
          print number_of_rocks
        """
               
        #If you collide with a gem, add 100 points to the score        
        if player.rect.colliderect(gem.rect):
            player.sndGem.play()
            score.score += 100
            gem.reset()
            
        #if you collide with a rock, lose a life
        rock_hit_list = pygame.sprite.spritecollide(player, rocks, False)
        for rock in rock_hit_list:
          rock.reset() 
          score.lives -= 1
          player.sndHit.play()
          
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
