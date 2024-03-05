import pygame


class Button:
    def __init__(self, surface, left, top, width, height):
        self.surface = surface
        self.backGround = (205, 205, 205)
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(left, top, width, height)
        self.text = "button1"
        self.font = pygame.font.Font(None, 24)
        self.image = None

    def set_backGround(self, color):
        self.backGround = color

    def set_color(self, color):
        self.color = color

    def set_text(self, text):
        self.text = text

    def set_image(self, image_path):
        margin = 10
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.rect.width - (margin + margin), self.rect.height - 50)
        )
        self.image_rect = self.image.get_rect(
            midtop=(self.rect.centerx, self.rect.top + margin)
        )

    def draw(self):
        if self.image is not None:
            pygame.draw.rect(self.surface, self.backGround, self.rect)
            self.surface.blit(self.image, self.image_rect)

        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(
            midtop=(self.rect.centerx, self.rect.bottom - 30)
        )
        self.surface.blit(text_surface, text_rect)

    def click(self, pos):
        return self.rect.collidepoint(pos)
