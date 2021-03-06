import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [640, 480]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_balls(object_list):
    ball = BouncingBall(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    ball = RainbowBall(SCREEN_SIZE, Vector2(200, 300), Vector2(3, 3), [0, 0, 0], 10)
    object_list.append(ball)

    ball = BouncingRainbow(SCREEN_SIZE, Vector2(300, 150), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    ball = KineticBall(object_list, SCREEN_SIZE, Vector2(100, 200), Vector2(1, 1), [0, 50, 255], 20)
    object_list.append(ball)

    ball = Ball(SCREEN_SIZE, Vector2(250, 250), Vector2(0, 0), [0, 255, 0], 10)
    object_list.append(ball)

    # TODO: Create other ball types for testing
    
def debug_create_blocks(object_list):
    pass
    # block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    # object_list.extend((block, ))

    # block = RainbowBlock(SCREEN_SIZE, Vector2(200,100), 60, 30, [255,255,0])
    # object_list.extend((block, ))
  
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy

    debug_create_balls(object_list)
    debug_create_blocks(object_list)

    run_me = True
 
    while run_me == True: # TODO:  Create more elegant condition for loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_me = False
        # Logic Loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  #TODO:  Get working
                if event.key == pygame.K_LEFT:
                    print("Pressed left")

        for obj in object_list:
            obj.update()
 
        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
    
 
if __name__ == "__main__":
    main()
