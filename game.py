import pygame

class Game():
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        
    def run(self):
        
        running = True
        while (running):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                    
game = Game()
game.run()