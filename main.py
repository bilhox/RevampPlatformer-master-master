import sys
import random
from os import path
import pygame

import maploader
from constants import *
from pygame.locals import *
from camera import Camera
from player import Player

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.Surface([DS_WIDTH , DS_HEIGHT])
mainclock = pygame.time.Clock()

class Game:
    def __init__(self):
        self.current_level_num = 0
        self.current_level = None
        self.running = False
    
    def start(self):
        self.create_level()
    
    def Update(self):
        
        self.events()
        if self.current_level != None:
            self.current_level.Update()
    
    def events(self):
        
        for event in pygame.event.get():
                 
            if self.current_level != None:
                self.current_level.event_handler(event)
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

    def create_level(self):
        self.current_level = Level(self.current_level_num)


class Level:
    def __init__(self, level_num):
        self.level_num = level_num
        self.entities = []
        self.particles = []
        

        self.running = False
        
        #self.map = maploader.Map(path.join(MAP_FOLDER, f"{level_num}.json"))
        #self.map = maploader.Map(path.join(MAP_FOLDER, "test.json"))
        self.width, self.height, entities, self.chunks = maploader.generate_map_data(path.join(MAP_FOLDER, "test.json"), CHUNK_SIZE)
        self.camera = Camera(DS_WIDTH , DS_HEIGHT)
        
        for entity in entities:
            if entity["name"] == "player":
                self.player = Player([entity["x"], entity["y"]])
        
        
    def Update(self):
        self.update()
        self.draw()

    def event_handler(self , event : pygame.event.Event):
        
        try:
            self.player.event_handler(event)
        except:
            pass

    def update(self):
        # for entity in self.entities.values():
        #     entity.update()
            #entity.animate()
        
        self.player.update()

        self.camera.focus(self.player)
    
    def draw(self):
             
        display_surface.fill([0,0,0])
        for chunk_data in self.chunks.values():
            for tile in chunk_data[0]:
                display_surface.blit(tile.image, [tile.pos[0] - self.camera.rect.x , tile.pos[1] - self.camera.rect.y])
        
        #for entity in self.entities[1:]:
            #DISPLAY_SURF.blit(entity.image, self.camera.apply(entity.rect))
        
        display_surface.blit(self.player.image, [self.player.rect.x - self.camera.rect.x , self.player.rect.y - self.camera.rect.y])
        screen.blit(pygame.transform.scale(display_surface, (WIDTH,HEIGHT)), (0,0))
        pygame.display.update()


"""
de
What I changed :

- Now the main loop of the program is on the main function
- In the Level and Game class , there is a new function called Update which call all the main functions of the class
- In the Game class , there is a new function called 'start' .
- Also added a new variable called player , it's more sample .
- In the Game class , there is a event_handler function called by the Update function , in this function
you have the main event when you want to quit the game , also this function call the event_handler function
from the current level , which also call all the event_handler functions of the entities . For now , it's probable
you didn't get it , but if later you have more levels and UI components for example , it'll be very usefull .
"""


def main():
    game = Game()
    game.start()
    
    while True:
        game.Update()


if __name__ == "__main__":
    main()