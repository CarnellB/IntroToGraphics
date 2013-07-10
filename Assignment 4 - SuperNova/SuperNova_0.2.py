import pygame
import random
pygame.init()

#set screen size
screen = pygame.display.set_mode((640, 480))

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
        
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("SuperNova Version 0.2")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player = Player()
    gem = Gem()
    
    allSprites = pygame.sprite.OrderedUpdates(gem,player)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()
            
