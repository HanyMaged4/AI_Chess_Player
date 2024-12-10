from config import Configrations
import pygame
class GameHelper:
    @staticmethod
    def get_mouse_pos(mouse_pos):
        mouse_x, mouse_y = mouse_pos
        square_size = Configrations.SQUARE_SIZE
        file = mouse_x // square_size
        rank = (mouse_y // square_size)
        if 0 <= file <= 7 and 0 <= rank <= 7:
            return file, rank
        return None, None

    @staticmethod
    def draw_board(screen):
        for x in range(8):
            for y in range(8):
                if ((x + y) % 2):
                    pygame.draw.rect(screen, Configrations.WHITE_COLOR,
                                     (x * Configrations.SQUARE_SIZE, y * Configrations.SQUARE_SIZE,
                                      Configrations.SQUARE_SIZE, Configrations.SQUARE_SIZE)
                                     )
                else:
                    pygame.draw.rect(screen, Configrations.BLACK_COLOR,
                                     (x * Configrations.SQUARE_SIZE, y * Configrations.SQUARE_SIZE,
                                      Configrations.SQUARE_SIZE, Configrations.SQUARE_SIZE)
                                     )