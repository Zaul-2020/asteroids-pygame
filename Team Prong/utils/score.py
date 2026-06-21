import pygame
import os

class score_bar():
    def __init__(self):
        self.score = 0


        # 1. Read file context safely
        if os.path.exists("utils/score.txt"):
            file_content = open("utils/score.txt", "r").read().strip()
            # 2. Check if the file content contains a valid number, otherwise default to 0
            self.high_score = int(file_content) if file_content.isdigit() else 0
        else:
            self.high_score = 0
            

        self.font = pygame.font.SysFont('comicsans', 20, bold=True)
        self.update_surface()

# ==============================================================================================================

    def update_surface(self):
        """Regenerates the text surface whenever the score changes."""
        self.text_surface = self.font.render(f"Score: {self.score} | High: {self.high_score}", True, 'yellow')

# ==============================================================================================================

    def add_point(self):
        """Adds a point and saves to file if high score is beaten."""
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            open("utils/score.txt", "w").write(str(self.high_score))
        self.update_surface()

# ==============================================================================================================

    def draw(self, screen):
        """Draws the score bar at the top-left of the screen."""
        screen.blit(self.text_surface, (20, 20))
        # ==============================================================================================================
