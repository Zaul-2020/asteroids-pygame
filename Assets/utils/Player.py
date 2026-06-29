import pygame

pygame.init()

class player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()

    self.origin_image = pygame.image.load('Assets/spaceship.png').convert()
    self.image = self.origin_image
    self.rect = self.image.get_rect()

    self.origin_image.set_colorkey((255, 255, 255))




# TODO: finish slide movement
# ========== spaceship movement logic ===========

# player attributes
    self.position = pygame.math.Vector2(x,y)
    self.velocity = pygame.math.Vector2(0,0)
    self.facing_dir = pygame.math.Vector2(0, -1)




# player constants
    self.turn_speed = 0.20
    self.acceleration = 1.2
    self.friction = 0.90
    self.max_speed = 14

  



  def move(self):
    self.keys = pygame.key.get_pressed()

    move_dir = pygame.math.Vector2(0, 0)



    if self.keys[pygame.K_UP]: move_dir.y -= 1
    if self.keys[pygame.K_DOWN]: move_dir.y += 1
    if self.keys[pygame.K_RIGHT]: move_dir.x += 1
    if self.keys[pygame.K_LEFT]: move_dir.x -= 1



    if move_dir.length() > 0:
      move_dir = move_dir.normalize()

      # FIXED: Shifting these lines inside the block locks rotation when you release keys
      self.facing_dir += (move_dir - self.facing_dir) * self.turn_speed
      self.facing_dir = self.facing_dir.normalize()


    self.velocity += move_dir * self.acceleration


    if self.velocity.length() > self.max_speed:
      self.velocity.scale_to_length(self.max_speed)

    

    angle = -pygame.math.Vector2(0, -1).angle_to(self.facing_dir)


    self.image = pygame.transform.rotate(self.origin_image, angle)

    old_center = self.rect.center
    self.rect = self.image.get_rect()
    self.rect.center = old_center


    self.velocity *= self.friction


    self.position += self.velocity
    self.rect.center = (int(self.position.x), int(self.position.y))
