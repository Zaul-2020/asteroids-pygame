import pygame
import utils.sprites_and_objects.paddle
import utils.sprites_and_objects.ball
import utils.score

pygame.init()

# =============================
def main():

    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Team Prong")

    clock = pygame.time.Clock()
# =====================================================
    paddle1 = utils.sprites_and_objects.paddle.paddle(10, screen_height//2 - 50, 1, 20)
    paddle2 = utils.sprites_and_objects.paddle.paddle(screen_width - 30, screen_height//2 - 50, 2, 20)

    ball = utils.sprites_and_objects.ball.ball(screen_width//2, screen_height//2, 25, 2)

    score_bar = utils.score.score_bar()
# =====================================================


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 0, 0))


        # --- DRAW OBJECTS ---
        screen.blit(paddle1.image, paddle1.rect)
        screen.blit(paddle2.image, paddle2.rect)
        screen.blit(ball.image, ball.rect)
        score_bar.draw(screen)



        # --- MOVEMENT ---
        paddle1.move()
        paddle2.move()
        ball.moving()
        ball.bounce()



        # --- COLLISIONS ---
        if ball.rect.colliderect(paddle1.rect):
            ball.velocity.x = abs(ball.velocity.x)
            if ball.velocity.length() < 15:
                ball.velocity *= 1.1
            score_bar.add_point()  # Changed from score += 1 to update text & high score safely



        if ball.rect.colliderect(paddle2.rect):
            ball.velocity.x = -abs(ball.velocity.x)
            if ball.velocity.length() < 15:
                ball.velocity *= 1.1
            score_bar.add_point()  # Changed from score += 1 to update text & high score safely



        # --- PONG SCORING CONDITION ---
        if ball.rect.left <= 0 or ball.rect.right >= screen_width:
            # Optional: You can choose to reset points here, or leave it as a penalty
            ball.rect.center = (screen_width // 2, screen_height // 2)
            ball.velocity.x *= -1



        pygame.display.flip()
        clock.tick(60)
        

# ==============================================

if __name__ == "__main__":
    main()

pygame.quit()
