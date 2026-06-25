import pygame

pygame.init()

class player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()

    self.image = pygame.image.load('Assets/spaceship.png').convert()
    self.rect = self.image.get_rect()


#   TODO: Add spaceship slide movement
    self.image.set_colorkey((255, 255, 255))
  
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
      self.rect.y += 10
    if keys[pygame.K_DOWN]:
      self.rect.y -= 10