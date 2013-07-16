import pygame
import random
pygame.init()

screen = pygame.display.set_mode((640, 480))
    
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
        self.dx = random.randrange(4, 8)
        
        
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
        
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("SuperNova Version 0.3")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    number_of_rocks = 3
    

    
    player = Player()
    gem = Gem()
    
    rocks = pygame.sprite.Group()
    
    for i in range(number_of_rocks):
      rock = BigRock()
      rocks.add(rock)
      
    
 
    space = Space()
    
    allSprites = pygame.sprite.OrderedUpdates(space,gem,player,rocks)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
                
        if player.rect.colliderect(gem.rect):
            player.sndGem.play()
            gem.reset()
            
           
        rock_hit_list = pygame.sprite.spritecollide(player, rocks, False)
        for rock in rock_hit_list:
          rock.reset() 
          print "HIT" 
          player.sndHit.play()
           

            
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
