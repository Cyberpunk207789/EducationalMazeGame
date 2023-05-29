# Класс для спрайта

import pygame


class Sprite (pygame.sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        if img != "none":
            imgs = pygame.image.load(img)
            self.img = pygame.transform.scale(imgs,(w, h))
            self.img.set_colorkey((0, 0, 0))
            self.rect = self.img.get_rect()
        else:
            self.img = None
            self.rect = pygame.Rect((self.x, self.y, self.w -10, self.h - 10))

        self.active = True

    def render(self, surface, debug):
        if self.active:
            surface.blit(self.img, (self.x, self.y))

            if debug:
                pygame.draw.rect(surface, (0, 0, 255), (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 0)

    def move_rect(self):
        if self.active:
            self.rect.x = self.x
            self.rect.y = self.y
            self.rect.width = self.w
            self.rect.height = self.h
