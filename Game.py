import pygame
from config import Configrations
from GameHelper import GameHelper
from ChessMoveValidator import ChessMoveValidator
class Game:
    def __init__(self,screen):
        self.screen = screen
        self.shapes = []
        self.pieces_name = ["b_pawn", "b_rook", "b_knight", "b_bishop", "b_queen", "b_king",
                            "w_pawn", "w_rook", "w_knight", "w_bishop", "w_queen", "w_king"]
        self.smaill_pieces = {}
        self.big_pieces = {}
        for p in self.pieces_name:
            self.smaill_pieces[p] = pygame.image.load(f"./assets/images/imgs-80px/{p}.png").convert_alpha()
            self.big_pieces[p] = pygame.image.load(f"./assets/images/imgs-128px/{p}.png").convert_alpha()
        self.postions =[["b_rook", "b_knight", "b_bishop", "b_queen", "b_king", "b_bishop", "b_knight", "b_rook"],
                        ["b_pawn"] * 8
                        ,["-"] * 8,["-"] * 8,["-"] * 8,["-"] * 8,
                        ["w_pawn"] * 8,
                        ["w_rook", "w_knight", "w_bishop", "w_queen", "w_king", "w_bishop", "w_knight", "w_rook"]]
        
        self.mouse_hold = None
        self.holdin_piece = None
        self.mouse_is_holding_piece = False

    def draw_postions(self):
        for r in range(8):
            for c in range(8):
                piece = self.postions[r][c]
                if piece != "-": #not empty
                    sqr = Configrations.SQUARE_SIZE
                    self.screen.blit(self.smaill_pieces[piece], (c * sqr, r * sqr))

        if(self.mouse_hold != None):

            rect = (self.mouse_hold[0] * Configrations.SQUARE_SIZE, self.mouse_hold[1] * Configrations.SQUARE_SIZE,
                        Configrations.SQUARE_SIZE,
                    Configrations.SQUARE_SIZE)
            pygame.draw.rect(self.screen, Configrations.HOLD_COLOR, rect)


    def handle_mouse_down(self,pos):
        x,y = GameHelper.get_mouse_pos(pos)
        if x is None or y is None:
            return
        if self.postions[x][y] != '-':
            self.mouse_hold = [y,x]
            self.holdin_piece = self.postions[x][y]
            self.mouse_is_holding_piece = True

    def handle_mouse_up(self,pos):
        if self.holdin_piece:
            x, y = GameHelper.get_mouse_pos(pos)
            if x is None or y is None:
                return

            start = (self.mouse_hold[1], self.mouse_hold[0])
            end = (x, y)
            piece = self.holdin_piece

            is_valid = False
            if piece.endswith("pawn"):
                is_valid = ChessMoveValidator.is_valid_pawn_move(start, end, piece, self.postions)
            elif piece.endswith("rook"):
                is_valid = ChessMoveValidator.is_valid_rook_move(start, end, piece, self.postions)
            elif piece.endswith("knight"):
                is_valid = ChessMoveValidator.is_valid_knight_move(start, end, piece, self.postions)
            elif piece.endswith("bishop"):
                is_valid = ChessMoveValidator.is_valid_bishop_move(start, end, piece, self.postions)
            elif piece.endswith("queen"):
                is_valid = ChessMoveValidator.is_valid_queen_move(start, end, piece, self.postions)
            elif piece.endswith("king"):
                is_valid = ChessMoveValidator.is_valid_king_move(start, end, piece, self.postions)

            if is_valid:
                self.postions[start[0]][start[1]] = '-'
                self.postions[end[0]][end[1]] = piece
                print(f"Move made: {piece} from {start} to {end}")
            else:
                print(f"Invalid move for {piece}")
            self.mouse_hold =None
            self.holdin_piece = None
            self.mouse_is_holding_piece = False

    def event_loop(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pygame.mouse.get_pos())

    def game_loop(self):
        GameHelper.draw_board(self.screen)
        self.draw_postions()

        if self.mouse_is_holding_piece :
            y,x = GameHelper.get_mouse_pos(pygame.mouse.get_pos())
            if x == None:
                return
            sqr = Configrations.SQUARE_SIZE
            piece_image = self.big_pieces[self.holdin_piece]
            piece_rect = piece_image.get_rect(center=(x * sqr + sqr // 2, y * sqr + sqr // 2))
            self.screen.blit(piece_image, piece_rect.topleft)