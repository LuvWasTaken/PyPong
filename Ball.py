import pygame

class Ball:
    RADIUS = 10

    def __init__(self, screen, x, y, velocityX, velocityY, fgColor, bgColor):
        self.x = x
        self.y = y
        self.screen = screen
        self.fgColor = fgColor
        self.bgColor = bgColor
        self.velocityX = velocityX
        self.velocityY = velocityY

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        print('x: %d y: %d' % (self.x, self.y))

        if self.x <= 20:
            self.velocityX = -self.velocityX

        if self.y <= 20:
            self.velocityY = -self.velocityY

        if self.y >= 380:
            self.velocityY = -self.velocityY

        self.show(self.bgColor)
        self.x = self.x + self.velocityX
        self.y = self.y + self.velocityY
        self.show(self.fgColor)








