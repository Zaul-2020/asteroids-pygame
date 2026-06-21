import pygame
import math
import random


# ==============================================================================
# 1. INITIALIZATION & SCREEN SETUP
# ==============================================================================
pygame.init()

screen_width = 600
screen_height = 600
screen_mid = 260

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

# FIXED: Replaced icontitle with Pygame's native set_icon method to properly display your asset
icon = pygame.image.load('Assets/icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()



# ==============================================================================
# 2. SCORE & UI SYSTEMS
# ==============================================================================
score_value = 0

try:
    with open("highscore.txt", "r") as f:
        high_score_value = int(f.read())
except:
    high_score_value = 0

game_font = pygame.font.SysFont(None, 30)

BG_img = pygame.image.load('Assets/background.png')
BG = pygame.transform.scale(BG_img, (600, 600))



# ==============================================================================
# 3. PLAYER CONFIGURATION
# ==============================================================================
spaceship_img = pygame.image.load('Assets/spaceship.png')
spaceship = pygame.transform.scale(spaceship_img, (80, 80))
spaceship_rect = spaceship.get_rect(topleft=(screen_mid, 300))



# ==============================================================================
# 4. WEAPONS CONFIGURATION
# ==============================================================================
bullet_speed = 40
blue_bullets = []

blue_Bullet = pygame.Surface((5, 20))
blue_Bullet.fill("yellow")

last_shot_time = 0         
shoot_cooldown = 400       



# ==============================================================================
# 5. ENEMY CONFIGURATION
# ==============================================================================
enemy_starty = 40
invaders_sine = 0

invaders_img = pygame.image.load('Assets/Invaders.png')
invaders = pygame.transform.scale(invaders_img, (70, 70))
invaders_rect = invaders.get_rect(topleft=(screen_mid, 0))

invaders_list = [
    {"rect": invaders_img.get_rect(topleft=(70, enemy_starty)),   "start_x": 70,  "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
    {"rect": invaders_img.get_rect(topleft=(140, enemy_starty)),  "start_x": 140, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
    {"rect": invaders_img.get_rect(topleft=(210, enemy_starty)), "start_x": 210, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
    {"rect": invaders_img.get_rect(topleft=(280, enemy_starty)), "start_x": 280, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)}, 
    {"rect": invaders_img.get_rect(topleft=(350, enemy_starty)), "start_x": 350, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
    {"rect": invaders_img.get_rect(topleft=(420, enemy_starty)), "start_x": 420, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)}
]



# ==============================================================================
# RESTART SYSTEM LOGIC FUNCTION
# ==============================================================================
def reset_game():
    global score_value, blue_bullets, invaders_list, invaders_sine
    
    score_value = 0
    invaders_sine = 0
    blue_bullets.clear()
    
    spaceship_rect.topleft = (screen_mid, 300)
    
    invaders_list = [
        {"rect": invaders_img.get_rect(topleft=(70, enemy_starty)),   "start_x": 70,  "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
        {"rect": invaders_img.get_rect(topleft=(140, enemy_starty)),  "start_x": 140, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
        {"rect": invaders_img.get_rect(topleft=(210, enemy_starty)), "start_x": 210, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
        {"rect": invaders_img.get_rect(topleft=(280, enemy_starty)), "start_x": 280, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)}, 
        {"rect": invaders_img.get_rect(topleft=(350, enemy_starty)), "start_x": 350, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
        {"rect": invaders_img.get_rect(topleft=(420, enemy_starty)), "start_x": 420, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)}
    ]



# ==============================================================================
# 6. MAIN GAME LOOP
# ==============================================================================
running = True

while running:
  print(spaceship_rect.x, spaceship_rect.y)

  clock.tick(60)
  screen.blit(BG, (0, 0))
  
  
  # --- DRAW PLAYER ---
  screen.blit(spaceship, spaceship_rect)


  # --- PLAYER WINDOW BOUNDS CHECK ---
  if spaceship_rect.top < 0 or spaceship_rect.bottom > 600:
     reset_game()


  # --- INFINITE RESPAWN SYSTEM ---
  if len(invaders_list) == 0:
      invaders_list = [
          {"rect": invaders_img.get_rect(topleft=(70, enemy_starty)),   "start_x": 70,  "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
          {"rect": invaders_img.get_rect(topleft=(140, enemy_starty)),  "start_x": 140, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
          {"rect": invaders_img.get_rect(topleft=(210, enemy_starty)), "start_x": 210, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
          {"rect": invaders_img.get_rect(topleft=(280, enemy_starty)), "start_x": 280, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)}, 
          {"rect": invaders_img.get_rect(topleft=(350, enemy_starty)), "start_x": 350, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)},
          {"rect": invaders_img.get_rect(topleft=(420, enemy_starty)), "start_x": 420, "float_y": float(enemy_starty), "speed": random.uniform(0.5, 2.0)}
      ]


  # --- UPDATE & DRAW ENEMIES ---
  invaders_sine += 0.05

  for enemy_data in invaders_list:
     enemys = enemy_data["rect"]
     
     enemy_data["float_y"] += enemy_data["speed"]
     enemys.y = int(enemy_data["float_y"])
     
     enemys.x = enemy_data["start_x"] + (math.sin(invaders_sine) * 40)

     if enemys.colliderect(spaceship_rect):
         reset_game()
         break

     if enemys.top > screen_height:
        enemy_data["float_y"] = -70.0
        enemys.y = -70
        enemy_data["speed"] = random.uniform(0.5, 2.0)
     
     screen.blit(invaders_img, enemys)


  # --- INPUT EVENT LISTENER ---
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        current_time = pygame.time.get_ticks()  
        
        if current_time - last_shot_time >= shoot_cooldown:
            new_bullet = blue_Bullet.get_rect(midbottom=spaceship_rect.midtop)
            blue_bullets.append(new_bullet)
            last_shot_time = current_time  


  # --- PLAYER REALTIME MOVEMENT CONTROLS ---
  keys = pygame.key.get_pressed()

  if keys[pygame.K_UP]:    spaceship_rect.y -= 15
  if keys[pygame.K_DOWN]:  spaceship_rect.y += 15
  if keys[pygame.K_RIGHT]: spaceship_rect.x += 10
  if keys[pygame.K_LEFT]:  spaceship_rect.x -= 10

  # FIXED: Compact 2-line edge boundary check
  if spaceship_rect.left < 0: spaceship_rect.left = 0
  if spaceship_rect.right > 600: spaceship_rect.right = 600


  # --- BULLET PHYSICS & DRAW ---
  for shots in blue_bullets[:]:
          shots.y -= bullet_speed

          if shots.bottom < 0:
            blue_bullets.remove(shots)
          else:
            screen.blit(blue_Bullet, shots)


  # --- BULLET-ENEMY COLLISION DETECTION ---
  for shots in blue_bullets[:]:
      for enemy_data in invaders_list[:]:
          if shots.colliderect(enemy_data["rect"]):
              blue_bullets.remove(shots)
              invaders_list.remove(enemy_data)
              
              score_value += 10
              if score_value > high_score_value:
                  high_score_value = score_value
                  with open("highscore.txt", "w") as f:
                      f.write(str(high_score_value))
              # FIXED: Restored complete keyword statement and loop closure layers
              break 


  # --- RENDER SCORE INTERFACE ---
  score_text = game_font.render(f"Score: {score_value}", True, "white")
  high_score_text = game_font.render(f"High Score: {high_score_value}", True, "white")
  
  screen.blit(score_text, (10, 10))
  screen.blit(high_score_text, (430, 10))


  # --- FRAME BUFFER REFRESH ---
  pygame.display.flip()


# ==============================================================================
# 7. ENGINE CLEANUP
# ==============================================================================
pygame.quit()
