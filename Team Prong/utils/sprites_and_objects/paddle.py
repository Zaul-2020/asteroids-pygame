import pygame
import utils.sprites_and_objects.ball

pygame.init()

# code of paddle1
# ===========================

class paddle(pygame.sprite.Sprite):
  def __init__(self, x, y, paddle_num, speed): # Renamed variable to avoid sharing the class name
      super().__init__()

      self.ball = utils.sprites_and_objects.ball.ball(800//2, 600//2, 25, 2)
      self.speed = speed
      self.x = x
      self.y = y
      self.paddle_num = paddle_num # FIX 1: Save it to self so move() can see it
      self.image = pygame.Surface((20, 100))
      self.image.fill('white')

      if self.paddle_num == 1:
        self.rect = self.image.get_rect(topleft=(x,y))
      if self.paddle_num == 2:
        self.rect = self.image.get_rect(topleft=(x,y))
    

# ==================
  def move(self):

    keys = pygame.key.get_pressed()

#  """"""""""""""""""""""""""""""""""""""""""""
    if self.paddle_num == 1: # FIX 1: Added self.



        if keys[pygame.K_w] and self.rect.top > 0:   # Pro-tip: Kept Player 1 on W/S so they don't fight over arrow keys
            self.rect.y -= self.speed # FIX 2: Fixed variable names

        if keys[pygame.K_s] and self.rect.bottom < 600:
            self.rect.y += self.speed

        if self.rect.top > 0:
           if self.ball.velocity.length() < 15:
                self.ball.velocity *= 1.1
        if self.rect.bottom < 600:
           if self.ball.velocity.length() < 15:
                self.ball.velocity *= 1.1
           
        


# """"""""""""""""""""""""""""""""""""""""""""""

    if self.paddle_num == 2: # FIX 1: Added self.

        if keys[pygame.K_UP] and self.rect.top > 0:   # Pro-tip: Kept Player 1 on W/S so they don't fight over arrow keys
            self.rect.y -= self.speed # FIX 2: Fixed variable names

        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed



# ==================

  def update(self):
    self.move()


# ==================
