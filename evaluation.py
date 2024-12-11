import chess

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
}

PAWN_TABLE = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 5, 5, 5, 5, 5, 5, 5,
    1, 1, 2, 3, 3, 2, 1, 1,
    0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5,
    0, 0, 0, 2, 2, 0, 0, 0,
    0.5, -0.5, -1, 0, 0, -1, -0.5, 0.5,
    0.5, 1, 1, -2, -2, 1, 1, 0.5,
    0, 0, 0, 0, 0, 0, 0, 0
]
KNIGHT_TABLE = [
    -50, -40, -30,  -30,  -30,  -30,  -40,  -50,
    -40, -20,   0,   0,    0,    0,   -20,  -40,
    -30,  0,    10,  15,   15,   10,   0,   -30,
    -30,  5,    15,  20,   20,   15,   5,   -30,
    -30,  0,    15,  20,   20,   15,   0,   -30,
    -30,  5,    10,  15,   15,   10,   5,   -30,
    -40, -20,   0,   5,    5,    0,   -20,  -40,
    -50, -40,  -30, -30,  -30,  -30,  -40,  -50,
]
BISHOP_TABLE = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,  10,  10,   5,   0, -10,
    -10,   5,   5,  10,  10,   5,   5, -10,
    -10,   0,  10,  10,  10,  10,   0, -10,
    -10,  10,  10,  10,  10,  10,  10, -10,
    -10,   5,   0,   0,   0,   0,   5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]
ROOK_TABLE = [
     0,   0,   0,   0,   0,   0,   0,   0,
     5,  10,  10,  10,  10,  10,  10,   5,
    -5,   0,   0,   0,   0,   0,   0,  -5,
    -5,   0,   0,   0,   0,   0,   0,  -5,
    -5,   0,   0,   0,   0,   0,   0,  -5,
    -5,   0,   0,   0,   0,   0,   0,  -5,
    -5,   0,   0,   0,   0,   0,   0,  -5,
     0,   0,   0,   5,   5,   0,   0,   0,
]
QUEEN_TABLE = [
    -20, -10, -10,  -5,  -5, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,   5,   5,   5,   0, -10,
     -5,   0,   5,   5,   5,   5,   0,  -5,
      0,   0,   5,   5,   5,   5,   0,  -5,
    -10,   5,   5,   5,   5,   5,   0, -10,
    -10,   0,   5,   0,   0,   0,   0, -10,
    -20, -10, -10,  -5,  -5, -10, -10, -20,
]
KING_TABLE = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
     20,  20,   0,   0,   0,   0,  20,  20,
     20,  30,  10,   0,   0,  10,  30,  20,
]

PIECE_SQUARE_TABLES = {
    chess.PAWN: PAWN_TABLE,
    chess.KNIGHT: KNIGHT_TABLE,
    chess.BISHOP: BISHOP_TABLE,
    chess.ROOK: ROOK_TABLE,
    chess.QUEEN: QUEEN_TABLE,
    chess.KING: KING_TABLE,
}

def evaluate_material(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = PIECE_VALUES.get(piece.piece_type, 0)
            score += value if piece.color == chess.WHITE else -value
    return score


def evaluate_position(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            table = PIECE_SQUARE_TABLES.get(piece.piece_type, [0] * 64)
            if piece.color == chess.WHITE:
                score += table[square]
            else:
                score -= table[chess.square_mirror(square)]
    return score


def value_state(board):
    material_score = evaluate_material(board)
    positional_score = evaluate_position(board)

    total_score = material_score + positional_score
    return total_score
