import pygame
import sys
from config import Configrations
from Game import Game
from GameStart import GameStartScreen

pygame.init()

screen = pygame.display.set_mode(Configrations.WINDOW)
pygame.display.set_caption(Configrations.TITLE)

def main():
    clock = pygame.time.Clock()
    beginner_game = Game(screen, 'beginner')
    advanced_game = Game(screen, 'advanced')
    start_screen = GameStartScreen(screen)
    on_start_screen = True
    game_type = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if on_start_screen:
                game_type = start_screen.handle_events(event)
                if game_type:  # Transition to game when a button is clicked
                    on_start_screen = False
            else:
                if game_type == 'beginner':
                    beginner_game.event_loop(event)
                elif game_type == 'advanced':
                    advanced_game.event_loop(event)

        if on_start_screen:
            start_screen.draw()
        else:
            if game_type == 'beginner':
                beginner_game.game_loop()
            elif game_type == 'advanced':
                advanced_game.game_loop()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
