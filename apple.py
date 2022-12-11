import pygame
from pygame.locals import *
from const import *
import random


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load(f"{ASSETS}/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):        

        # clearing the screen
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        # Calculate the new random position keep in the boundaries of the screen
        # The -1 is to avoid to appear exactly in the border of the screen
        self.x = random.randint(0, WINDOWS_WIDTH/SIZE-1)*SIZE
        self.y = random.randint(0, WINDOWS_HEIGHT/SIZE-1)*SIZE

