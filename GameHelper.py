from config import Configrations
import pygame
class GameHelper:
    @staticmethod
    def get_mouse_pos(pos):
        x = int(pos[1] / Configrations.SQUARE_SIZE)
        y = int(pos[0] / Configrations.SQUARE_SIZE)
        if(x < 8 and y < 8 and x>=0 and y >= 0 ):
            return [x,y]
        return [None,None]

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