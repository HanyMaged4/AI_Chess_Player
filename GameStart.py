import pygame

class GameStartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, 100)
        self.button_font = pygame.font.Font(None, 50)
        self.title_text = "Chess Game"
        self.beginner_button_text = "Beginner"
        self.advanced_button_text = "Advanced"
        self.title_color = (255, 255, 255)
        self.button_color = (0, 128, 255)
        self.button_hover_color = (0, 102, 204)
        self.button_text_color = (255, 255, 255)

        self.button_width = 200
        self.button_height = 60

        self.beginner_button_rect = pygame.Rect(
            (self.screen.get_width() // 2 - self.button_width - 20),
            (self.screen.get_height() // 2 + 100),
            self.button_width,
            self.button_height
        )

        self.advanced_button_rect = pygame.Rect(
            (self.screen.get_width() // 2 + 20),
            (self.screen.get_height() // 2 + 100),
            self.button_width,
            self.button_height
        )

    def draw(self):
        self.screen.fill((0, 0, 0))

        title_surface = self.title_font.render(self.title_text, True, self.title_color)
        title_rect = title_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 100))
        self.screen.blit(title_surface, title_rect)

        mouse_pos = pygame.mouse.get_pos()

        beginner_button_color = self.button_hover_color if self.beginner_button_rect.collidepoint(mouse_pos) else self.button_color
        advanced_button_color = self.button_hover_color if self.advanced_button_rect.collidepoint(mouse_pos) else self.button_color

        pygame.draw.rect(self.screen, beginner_button_color, self.beginner_button_rect)
        pygame.draw.rect(self.screen, advanced_button_color, self.advanced_button_rect)

        beginner_text_surface = self.button_font.render(self.beginner_button_text, True, self.button_text_color)
        beginner_text_rect = beginner_text_surface.get_rect(center=self.beginner_button_rect.center)
        self.screen.blit(beginner_text_surface, beginner_text_rect)

        advanced_text_surface = self.button_font.render(self.advanced_button_text, True, self.button_text_color)
        advanced_text_rect = advanced_text_surface.get_rect(center=self.advanced_button_rect.center)
        self.screen.blit(advanced_text_surface, advanced_text_rect)

        pygame.display.flip()

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.beginner_button_rect.collidepoint(event.pos):
                return "beginner"
            if self.advanced_button_rect.collidepoint(event.pos):
                return "advanced"
        return None
