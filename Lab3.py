import pygame
import random
from Ball import Ball
from Paddle import Paddle

def main():
    pygame.init()
    pygame.display.set_caption("My Pong")

    width = 800
    height = 400
    velocity = 5
    FPS = 60

    screen = pygame.display.set_mode((width, height))
    screen.fill((0,0,0))

    pygame.display.update()

    colorOfWall = pygame.Color("red")
    bgColor = pygame.Color("black")

    border = 10

    pygame.draw.rect(screen, colorOfWall, pygame.Rect((0,0),(width, border)))
    pygame.draw.rect(screen, colorOfWall, pygame.Rect((0,0),(border, height)))
    pygame.draw.rect(screen, colorOfWall, pygame.Rect((0, height - border),(width, border)))

    x0 = width - Ball.RADIUS
    y0 = height // 2

    vx0 = -velocity
    vy0 = velocity * random.choice([-1, 1])

    ball0 = Ball(screen, x0, y0, vx0, vy0, pygame.Color("red"), bgColor)
    ball0.show(pygame.Color("red"))

    pygame.display.update()

    running = True

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(FPS)
        ball0.update()

if __name__ == "__main__":
    main()
