class ChessMoveValidator:

    @staticmethod
    def is_friendly_piece(piece, target_piece):
        return piece.startswith('b') and target_piece.startswith('b') or piece.startswith('w') and target_piece.startswith('w')

    @staticmethod
    def is_valid_pawn_move(start, end, piece, board):
        if ChessMoveValidator.is_friendly_piece(piece, board[end[0]][end[1]]):
            return False
        start_row, start_col = start
        end_row, end_col = end
        direction = 1 if piece.startswith('b_') else -1
        if start_col == end_col and board[end_row][end_col] == "-":
            if end_row == start_row + direction:
                return True
        if start_col == end_col and board[end_row][end_col] == "-":
            if (piece.startswith('b_') and start_row == 1) or (piece.startswith('w_') and start_row == 6):
                if end_row == start_row + 2 * direction:
                    return board[start_row + direction][start_col] == "-"
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            if board[end_row][end_col] != "-" and not ChessMoveValidator.is_friendly_piece(piece,
                                                                                           board[end_row][end_col]):
                return True
        return False

    @staticmethod
    def is_valid_rook_move(start, end, piece, board):
        if ChessMoveValidator.is_friendly_piece(piece, board[end[0]][end[1]]):
            return False
        start_row, start_col = start
        end_row, end_col = end
        if start_row == end_row:
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] != "-":
                    return False
            return True
        if start_col == end_col:
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] != "-":
                    return False
            return True
        return False

    @staticmethod
    def is_valid_knight_move(start, end, piece, board):
        if ChessMoveValidator.is_friendly_piece(piece, board[end[0]][end[1]]):
            return False
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    @staticmethod
    def is_valid_bishop_move(start, end, piece, board):
        if ChessMoveValidator.is_friendly_piece(piece, board[end[0]][end[1]]):
            return False
        start_row, start_col = start
        end_row, end_col = end
        if abs(start_row - end_row) != abs(start_col - end_col):
            return False
        step_row = 1 if end_row > start_row else -1
        step_col = 1 if end_col > start_col else -1
        for i in range(1, abs(start_row - end_row)):
            if board[start_row + i * step_row][start_col + i * step_col] != "-":
                return False
        return True

    @staticmethod
    def is_valid_queen_move(start, end, piece, board):
        return (
                ChessMoveValidator.is_valid_rook_move(start, end,piece, board) or
                ChessMoveValidator.is_valid_bishop_move(start, end,piece, board)
        )

    @staticmethod
    def is_valid_king_move(start, end, piece, board):
        if ChessMoveValidator.is_friendly_piece(piece, board[end[0]][end[1]]):
            return False
        start_row, start_col = start
        end_row, end_col = end
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return row_diff <= 1 and col_diff <= 1