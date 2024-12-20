import pygame
from config import Configrations
from GameHelper import GameHelper
import chess
from minimax import find_best_move
from minimax2 import find_best_move2
class Game:
    def __init__(self, screen,type):
        self.type = type
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
        self.font = pygame.font.Font(None, 74)
        self.game_over_message = "GAME OVER !"
        self.game_win_message = "WINNER !"
        self.game_draw_message = "DRAW !"
        self.checkmate_sound = pygame.mixer.Sound('./assets/sounds/checkmate.wav')
        self.move_sound = pygame.mixer.Sound('./assets/sounds/move.wav')
        self.capture_sound =pygame.mixer.Sound('./assets/sounds/capture.wav')

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
            promotion = None

            if self.board.piece_at(start_square).piece_type == chess.PAWN:
                if (chess.square_rank(end_square) == 7 and chess.square_rank(start_square) == 6) or\
                        (chess.square_rank(end_square) == 0 and chess.square_rank(start_square) == 1):
                    promotion = chess.QUEEN

            move = chess.Move(start_square, end_square, promotion=promotion)

            if move in self.board.legal_moves:
                if self.board.is_capture(move):
                    self.capture_sound.play()
                else:
                    self.move_sound.play()
                self.board.push(move)


                if not self.board.is_game_over():
                    move = ' ';
                    if self.type  == 'advanced' :
                        move = find_best_move(self.board, depth=3)
                    else:
                        move = find_best_move2(self.board, depth=3)
                    print(f'move : {move}')

                    if self.board.is_capture(move):
                       self.capture_sound.play()

                    self.board.push(move)
                        
                else:
                    if self.board.is_stalemate():
                        text_surface = self.font.render(self.game_draw_message, True, (0, 255, 0))  
                        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
                        self.screen.blit(text_surface, text_rect) 
                        pygame.display.flip()  
                        print('DRAW')
                        self.capture_sound.play()
                        pygame.time.wait(3000)
                        exit()
                    if self.board.is_game_over():
                        text_surface = self.font.render(self.game_win_message, True, (0, 0, 255))  # Red color
                        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
                        self.screen.blit(text_surface, text_rect) 
                        pygame.display.flip()  
                        print('WINNER')
                        self.checkmate_sound.play()
                        pygame.time.wait(3000)
                        exit()
            else:
                if self.board.is_stalemate():
                        text_surface = self.font.render(self.game_draw_message, True, (0, 255, 0))  
                        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
                        self.screen.blit(text_surface, text_rect) 
                        pygame.display.flip()  
                        print('DRAW')
                        self.capture_sound.play()
                        pygame.time.wait(3000)
                        exit()
                if self.board.is_game_over():
                    text_surface = self.font.render(self.game_over_message, True, (255, 0, 0))
                    text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
                    self.screen.blit(text_surface, text_rect)  
                    pygame.display.flip() 
                    self.checkmate_sound.play()
                    pygame.time.wait(3000)
                    print('GAME OVER!')
                    exit()
                else:
                    print('illegal move')
            
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
        if self.mouse_is_holding_piece and not self.board.is_game_over():
            # print('dsds')
            x, y = GameHelper.get_mouse_pos(pygame.mouse.get_pos())
            if x is None:
                return
            sqr = Configrations.SQUARE_SIZE
            piece_image = self.big_pieces[self.holdin_piece.symbol()]
            piece_rect = piece_image.get_rect(center=(x * sqr + sqr // 2, y * sqr + sqr // 2))
            self.screen.blit(piece_image, piece_rect.topleft)