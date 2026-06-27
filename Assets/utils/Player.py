import pygame

pygame.init()

class player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()

    self.image = pygame.image.load('Assets/spaceship.png').convert()
    self.rect = self.image.get_rect()

    self.rect.center = (x,y)


#   TODO: Add spaceship slide movement
    self.image.set_colorkey((255, 255, 255))
  

  def move(self):
      keys = pygame.key.get_pressed()

      if keys[pygame.K_UP]:
        self.rect.y -= 10
      if keys[pygame.K_DOWN]:
        self.rect.y += 10
      if keys[pygame.K_RIGHT]:
        self.rect.x += 10
      if keys[pygame.K_LEFT]:
        self.rect.x -= 10