import pygame
import sys
from config import Configrations
from Game import Game

pygame.init()

screen = pygame.display.set_mode(Configrations.WINDOW)
pygame.display.set_caption(Configrations.TITLE)

def main():
    clock = pygame.time.Clock()
    game = Game(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game.event_loop(event)
        game.game_loop()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
