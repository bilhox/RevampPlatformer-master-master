import pygame

from pygame.locals import *
from constants import *

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.size = [8 , 12]
        self.velocity = pygame.math.Vector2(0,0)
        self.image = pygame.Surface(self.size.copy())
        self.image.fill("red")
        
        self.key_pressed = {"right":False , "left":False , "up":False}

    @property
    def rect(self):
        return Rect(self.pos[0] // 1 , self.pos[1] // 1 , self.size[0] , self.size[1])
    
    def event_handler(self , event : pygame.event.Event):
             
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.key_pressed["right"] = True
            if event.key == K_LEFT:
                self.key_pressed["left"] = True
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                self.key_pressed["right"] = False
            if event.key == K_LEFT:
                self.key_pressed["left"] = False
        
    def move(self , movement : pygame.math.Vector2):
        self.pos[0] += movement.x
        self.pos[1] += movement.y

    def update(self): 
        
        movement = pygame.math.Vector2(self.velocity.x , self.velocity.y)
        
        if self.key_pressed["right"]:
            movement.x += 1
        elif self.key_pressed["left"]:
            movement.x -= 1
        
        self.move(movement)
    