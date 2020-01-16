import pygame
import os

pygame.init()
HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'data')
player_img = pygame.image.load(os.path.join(img_folder, 'ship.jpg')).convert()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x, self.y = 100, 100
        self.rect.center = (self.x, self.y)

    def update_right(self):
        if self.x <= 400:
            self.x += 2
        self.rect.center = (self.x, self.y)




all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

pygame.display.update()

run = True
while run:
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update()


    screen.fill((255, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()