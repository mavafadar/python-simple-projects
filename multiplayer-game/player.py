import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rectangle = (x, y, width, height)
        self.value = 1

    def update_rectangle(self):
        self.rectangle = (self.x, self.y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rectangle)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.value
        if keys[pygame.K_RIGHT]:
            self.x += self.value
        if keys[pygame.K_UP]:
            self.y -= self.value
        if keys[pygame.K_DOWN]:
            self.y += self.value
        self.update_rectangle()
