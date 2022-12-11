import pygame
from pygame.locals import *
from const import *

class Snake:
    def __init__(self, parent_screen, length):

        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load(f"{ASSETS}/block.jpg").convert()
        # initialize an array of the size of the length parameter
        self.x, self.y = [SIZE] * length, [SIZE] * length
        self.direction = 'down'

    def walk(self):

        # we must position each block in the previous position of the previous block
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        self.draw()
    
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):

        # clearing the screen
        # self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'
