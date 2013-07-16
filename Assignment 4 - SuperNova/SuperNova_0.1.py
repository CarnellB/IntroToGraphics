import pygame
pygame.init()
"""
Source File Name: SuperNova_0.1.py
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
                  SuperNova_0.7 - scoring added
                  SuperNova_0.8 - intro screen added
"""
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
        
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("SuperNova Version 0.1")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player = Player()
    
    allSprites = pygame.sprite.Group(player)
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
            
