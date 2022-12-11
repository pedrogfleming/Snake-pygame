import pygame
from pygame.locals import *
import time
import snake
import apple
from const import *


class Game:

    def __init__(self):
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Snake And Apple Game")

        pygame.mixer.init()
        self.play_background_music()
        # Create a Pygame window
        self.surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
        self.snake = snake.Snake(self.surface, INITIAL_SNAKE_LENGTH)
        self.snake.draw()
        self.apple = apple.Apple(self.surface)
        self.apple.draw()
        self.speed = INITIAL_SPEED_SNAKE

    def is_collision(self, x1, y1, x2, y2):
        return x1 == x2 and y1 == y2        

    def is_border_collision(self, snake_x, snake_y):
        return snake_x < 0 or snake_y < 0 or snake_x >= WINDOWS_WIDTH or snake_y >= WINDOWS_HEIGHT

    def play_background_music(self):
        pygame.mixer.music.load(f"{ASSETS}/bg_music_1.mp3")
        pygame.mixer.music.play()   

    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"{ASSETS}/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        bg = pygame.image.load(f"{ASSETS}/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_border_collision(self.snake.x[0], self.snake.y[0]):
            self.play_sound("crash")
            raise "Game over"

        # snake colliding with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()
            if self.speed > 0.1:
                self.speed -= 0.1

        # snake colliding with itself
        # it will never collide with 1 and 2 blocks
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Game over"

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        # Display top right corner
        self.surface.blit(score, (800, 10))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game over! Your score is: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit, press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))        
        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        self.snake = snake.Snake(self.surface, INITIAL_SNAKE_LENGTH)
        self.apple = apple.Apple(self.surface)
        self.speed = INITIAL_SPEED_SNAKE

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.type == QUIT:
                        running = False
                        break
                    if event.key == K_SPACE:
                        print(f"x:{self.snake.x[0]} y:{self.snake.y[0]}")
                    if event.key == K_RETURN:
                        pause = False
                        pygame.mixer.music.unpause()

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()                            
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(self.speed)