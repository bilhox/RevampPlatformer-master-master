from pygame import Rect
from constants import *

class Camera:
    def __init__(self, width, height):
        self.rect = Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def focus(self, target):
        x = target.rect.x - (DS_WIDTH // 2) - target.rect.w // 2
        y = target.rect.y - (DS_HEIGHT // 2) - target.rect.h // 2
        
        x = min(max(0,x),DS_WIDTH+self.width)
        y = min(max(0,y),DS_HEIGHT+self.height)
        
        self.rect.x , self.rect.y = x , y