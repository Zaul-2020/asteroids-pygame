import pygame
import Assets.utils.Player

pygame.init()


def main():
  screen_width = 800
  screen_height = 768

  screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
  pygame.display.set_caption('Game')

  clock = pygame.time.Clock()


  player = Assets.utils.Player.player(screen_width//2, screen_height//2)


  running = True
  while running:
    clock.tick(60)

    screen.fill('light blue')
    screen.blit(player.image, player.rect)

    player.move()

    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        running = False
      
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
        

    pygame.display.flip()

  pygame.quit()

if __name__ == "__main__":
  main()