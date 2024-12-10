import chess
from evaluation import vlaue_state

def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing):

    if depth == 0 or board.is_game_over():
        return vlaue_state(board)

    legal_moves = list(board.legal_moves)

    if is_maximizing:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board, depth):
    best_move = None
    max_eval = float('-inf')

    for move in board.legal_moves:
        board.push(move)
        eval = minimax_alpha_beta(board, depth - 1, float('-inf'), float('inf'), False)
        board.pop()

        if eval > max_eval:
            max_eval = eval
            best_move = move

    return best_move
