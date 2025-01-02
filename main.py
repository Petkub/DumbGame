import pygame
from paddle2 import *

class Game():
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        
        self.bg_img = pygame.image.load("images/bg.jpeg")
        self.bg_img = pygame.transform.scale(self.bg_img, (800, 600))
        
        self.pad_img = pygame.image.load("images/paddle.png")
        self.pad_img = pygame.transform.scale(self.pad_img, (96, 30))
        
        #paddle's object
        self.paddle = Paddle(self.window, self.pad_img, 350, 500)
        
        
    def run(self):
        running = True
        
        while (running == True):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            #render
            self.window.blit(self.bg_img, (0, 0))
            self.paddle.draw()
            
            pygame.display.update()


game = Game()
game.run()
                    