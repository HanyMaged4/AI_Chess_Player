import pygame
from config import Configrations
from GameHelper import GameHelper
import chess
from minimax import find_best_move
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.pieces_name = ["p", "r", "n", "b", "q", "k", "P", "R", "N", "B", "Q", "K"]
        self.smaill_pieces = {}
        self.big_pieces = {}
        for p in self.pieces_name:
            if p.islower():
                self.smaill_pieces[p] = pygame.image.load(f"./assets/images/imgs-80px/black/{p}.png").convert_alpha()
                self.big_pieces[p] = pygame.image.load(f"./assets/images/imgs-128px/black/{p}.png").convert_alpha()
            else:
                self.smaill_pieces[p] = pygame.image.load(f"./assets/images/imgs-80px/white/{p}.png").convert_alpha()
                self.big_pieces[p] = pygame.image.load(f"./assets/images/imgs-128px/white/{p}.png").convert_alpha()
        self.mouse_hold = None
        self.holdin_piece = None
        self.mouse_is_holding_piece = False
        self.board = chess.Board()

    def draw_positions(self):
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                r, c = divmod(square, 8)
                sqr = Configrations.SQUARE_SIZE
                pos = (c * sqr, r * sqr)
                self.screen.blit(self.smaill_pieces[piece.symbol()], pos)

        if self.mouse_hold is not None:
            rect = (
                self.mouse_hold[0] * Configrations.SQUARE_SIZE,
                self.mouse_hold[1] * Configrations.SQUARE_SIZE,
                Configrations.SQUARE_SIZE,
                Configrations.SQUARE_SIZE,
            )
            pygame.draw.rect(self.screen, Configrations.HOLD_COLOR, rect)

    def handle_mouse_down(self, pos):
        y,x = GameHelper.get_mouse_pos(pos)
        if x is None or y is None:
            return
        square = chess.square(y, x)
        piece = self.board.piece_at(square)
        print(piece)
        if piece:
            self.mouse_hold = [y, x]
            self.holdin_piece = piece
            self.mouse_is_holding_piece = True

    def handle_mouse_up(self, pos):
        if self.holdin_piece:
            y, x = GameHelper.get_mouse_pos(pos)
            if x is None or y is None:
                return
            start_square = chess.square(self.mouse_hold[0], self.mouse_hold[1])
            end_square = chess.square(y, x)
            move = chess.Move(start_square, end_square)
            print(f'from {start_square} to {end_square} || {move}')
            # print(self.board.legal_moves)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.board.push(find_best_move(self.board, depth=5))
            self.mouse_hold = None
            self.holdin_piece = None
            self.mouse_is_holding_piece = False

    def event_loop(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pygame.mouse.get_pos())

    def game_loop(self):
        GameHelper.draw_board(self.screen)
        self.draw_positions()
        if self.mouse_is_holding_piece:
            # print('dsds')
            x, y = GameHelper.get_mouse_pos(pygame.mouse.get_pos())
            if x is None:
                return
            sqr = Configrations.SQUARE_SIZE
            piece_image = self.big_pieces[self.holdin_piece.symbol()]
            piece_rect = piece_image.get_rect(center=(x * sqr + sqr // 2, y * sqr + sqr // 2))
            self.screen.blit(piece_image, piece_rect.topleft)
