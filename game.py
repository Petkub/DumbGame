import pygame
import pygame.locals
from paddle import *
from ball import *
from block import *

class Game():
    
    def __init__(self):
        pygame.init()
        ###WINDOW + BLACKGROUND
        self.window = pygame.display.set_mode((800, 600))
        self.bg = pygame.image.load("images/bg.jpeg")
        self.bg = pygame.transform.scale(self.bg, (800, 600))
        ###
        
        ###paddle        
        self.paddle_img = pygame.image.load("images/paddle.png")
        self.paddle_img = pygame.transform.scale(self.paddle_img, (96, 30))
        self.paddle = Paddle(self.window, 350, 450, self.paddle_img)
        ###
        
        ###ball
        self.ball_img = pygame.image.load("images/ball.png")
        self.ball_img = pygame.transform.scale(self.ball_img, (32, 32))
        self.ball = Ball(self.window, self.ball_img, 350, 330)
        ###
        
        ###block
        
        ###
        
        ###time
        self.clock = pygame.time.Clock()
        ###
        
        ###state
        
        ###
        
        ###font & text
        
        ###
        
    #1 RUN method
    def run(self):
        
        running = True
        while (running):
            
            '''delta time'''
            delta_time = self.clock.tick(60) / 1000
            pressed = pygame.key.get_pressed()
            
            #EVENT CHECKER
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            ###RENDERING
            self.window.blit(self.bg, (0, 0))
            self.paddle.draw()
            self.ball.draw()
            
            self.paddle.move(delta_time)
            self.ball.move(delta_time)
            ###
            
            pygame.display.update()
            
    #2 BlOCK X_POSITION method
    def cal_block_Xpos(self):
        pass
    ###
    
    #3 BlOCK Y_POSITION method
    def cal_block_YPos(self):
        pass
    ###
    
    #4 Ball & Block checker method
    def ball_block_collision(self):
        pass
    ###
    
    #5 WIN & Game Over checker method
    def game_checker(self):
        pass
    ###
    
    #6 Text Display method
    def display(self):
        pass
    ###
                    
#MAIN GAME                    
game = Game()
game.run()