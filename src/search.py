
from copy import deepcopy
import chess

from src.evaluation import evaluate

def search(board: chess.Board, depth: int, move_stack: tuple = ()):
    print("--------------")
    print(f"depth = {depth}")
    print(f"move_stack = {move_stack}")
    print(board)
    print(board.turn)

    if depth == 0:
        evaluation = evaluate(board)
        print(f"evaluating = {evaluation}")
        return (evaluation, move_stack)

    legal_moves = board.legal_moves

    moves_evaluations_map = {}
    # evaluations = []

    for legal_move in legal_moves:
        print("--")
        # print(f"pushing step {legal_move}")
        board_copy = deepcopy(board)
        board_copy.push_san(str(legal_move))

        recursive_evaluation, recursive_move_stack = search(board_copy, depth-1, move_stack + (str(legal_move), ))
        moves_evaluations_map[recursive_move_stack] = recursive_evaluation
        # evaluations.append(search(board_copy, depth-1, move_stack + [str(legal_move)]))
        
        # move, evaluation = search(board_copy, depth-1)
        # evaluation = search(board_copy, depth-1)
        # evaluations.append(evaluation)

        # moves_evaluations_map[str(legal_move)] = search(board_copy, depth-1)

    

    if depth % 2 == 0:
        max_evaluation = max(moves_evaluations_map.values())
        move_stack_max_evaluation = [move_stack for move_stack, evaluation in moves_evaluations_map.items() if evaluation == max_evaluation][0]
        return max_evaluation, move_stack_max_evaluation
    
    min_evaluation = min(moves_evaluations_map.values())
    move_stack_min_evaluation = [move_stack for move_stack, evaluation in moves_evaluations_map.items() if evaluation == min_evaluation][0]
    return min_evaluation, move_stack_min_evaluation
    

if __name__ == "__main__":
    board = chess.Board("q1n5/1P5p/8/6k1/8/8/8/7K w - - 0 1")
    search_result = search(board, 2)
    best_move = search_result[1][0]
    print(search_result)
    print(best_move)
