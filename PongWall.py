import pygame

pygame.init()
pygame.display.set_caption("My Pong")

width = 800
height = 400

screen = pygame.display.set_mode((width, height))
screen.fill((0,0,0))

pygame.display.update()

colorOfWall = pygame.Color("red")
border = 10

pygame.draw.rect(screen, colorOfWall, pygame.Rect((0,0),(width, border)))
pygame.draw.rect(screen, colorOfWall, pygame.Rect((0,0),(border, height)))
pygame.draw.rect(screen, colorOfWall, pygame.Rect((0, height - border),(width, border)))

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
