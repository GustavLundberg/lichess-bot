
from copy import deepcopy
import chess

from evaluation import Evaluate

def search(board: chess.Board, depth: int):
    print("--------------")
    print(f"depth = {depth}")
    print(board)
    print(board.turn)

    if depth == 0:
        evaluation = Evaluate(board)
        print(f"evaluating = {evaluation}")
        return evaluation

    legal_moves = board.legal_moves

    moves_evaluations_map = {}
    evaluations = []

    for legal_move in legal_moves:
        print("--")
        print(f"pushing step {legal_move}")
        board_copy = deepcopy(board)
        board_copy.push_san(str(legal_move))
        evaluations.append(search(board_copy, depth-1))
        
        # move, evaluation = search(board_copy, depth-1)
        # evaluation = search(board_copy, depth-1)
        # evaluations.append(evaluation)

        # moves_evaluations_map[str(legal_move)] = search(board_copy, depth-1)

    

    if depth % 2 == 0:
        return max(evaluations)
    
    return min(evaluations)

if __name__ == "__main__":
    board = chess.Board("7k/3p4/2P5/8/8/8/8/7K w - - 0 1")
    result = search(board, 2)
    print(result)
