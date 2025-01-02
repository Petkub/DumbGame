import pygame

class Paddle():
    
    def __init__(self, window, image, x, y):
        self.window = window
        self.pad_img = image
        self.pad_rect = self.pad_img.get_rect(x = x, y = y)
        
    def draw(self):
        self.window.blit(self.pad_img, (self.pad_rect.x, self.pad_rect.y))
        self.move()
        
    def move(self):
        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_a]):
            self.pad_rect.x -= 1
        if (pressed[pygame.K_d]):
            self.pad_rect.x += 1