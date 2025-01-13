import pygame
#Paddle.py

class Ball():
    def __init__(self, window, image, x, y):
        self.window = window
        self.image = image
        self.ball_rect = self.image.get_rect(x = x, y = y)
        
        self.velocity_x = 200
        self.velocity_y = 200
        
    def draw(self):
        self.window.blit(self.image, (self.ball_rect.x, self.ball_rect.y))
        
    def move(self, delta_time):
        self.bound_checking()
        self.ball_rect.x += self.velocity_x * delta_time
        self.ball_rect.y += self.velocity_y * delta_time
        
    def bound_checking(self):
        #TOP
        if (self.ball_rect.x <= 0):
            self.ball_rect.x = 0
            self.velocity_x *= -1
        #RIGHT
        if (self.ball_rect.x >= self.window.get_width() - self.ball_rect.w):
            self.ball_rect.x = self.window.get_width() - self.ball_rect.w
            self.velocity_x *= -1
        #LEFT
        if (self.ball_rect.y <= 0):
            self.ball_rect.y = 0
            self.velocity_y *= -1
        #Paddle & Ball
        
        ###
        '''TEST'''
        # if (self.ball_rect.y >= self.window.get_height() - self.ball_rect.h):
        #     self.ball_rect.y = self.window.get_height() - self.ball_rect.h
        #     self.velocity_y *= -1
        