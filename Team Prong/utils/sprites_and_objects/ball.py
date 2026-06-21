import random
import pygame

pygame.init()

class ball(pygame.sprite.Sprite):
  def __init__(self, x, y, radius, speed):
    super().__init__()
    
    self.x = x
    self.y = y
    self.radius = radius
    self.diameter = radius * 2
    self.speed = speed

    self.random_angle = random.randint(0, 360)
    self.velocity = pygame.math.Vector2(speed, 0).rotate(self.random_angle)

    self.image = pygame.Surface((self.diameter, self.diameter), pygame.SRCALPHA)
    pygame.draw.circle(self.image, 'gray', (self.radius, self.radius), self.radius)

    self.rect = self.image.get_rect(topleft=(x, y))

  def moving(self):

    self.rect.x += self.velocity.x
    self.rect.y += self.velocity.y

  
  
  def bounce(self):
      # ================================= Bounce off top and bottom walls
      if self.rect.top <= 0 or self.rect.bottom >= 600:
          self.velocity.y *= -1
          


      # ================================= Bounce off left and right walls
      if self.rect.left <= 0 or self.rect.right >= 800:
          print('you lost')
          self.rect.center = (800/2, 600/2)
          self.velocity = pygame.math.Vector2(self.speed, 0).rotate(self.random_angle)
