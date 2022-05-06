import pygame


pygame.font.init()


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont('Bahnschrift', 20)
        text = font.render(self.text, 1, (255, 255, 255))
        window.blit(
            text,
            (
                self.x + round(self.width / 2) - round(text.get_width() / 2),
                self.y + round(self.height / 2) - round(text.get_height() / 2)
            )
        )

    def click(self, position):
        x_one = position[0]
        y_one = position[1]
        if self.x <= x_one <= self.x + self.width and self.y <= y_one <= self.y + self.height:
            return True
        return False
