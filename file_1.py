import pygame
import os

pygame.init()
HEIGHT, MIGHT = 500, 500
screen = pygame.display.set_mode((MIGHT, HEIGHT))

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
image = load_image('bomb.png')
image = pygame.transform.scale(image, (200, 100))

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image('bomb.png')
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
sprite.rect.x = 50
sprite.rect.y = 300


run = True
while run:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
