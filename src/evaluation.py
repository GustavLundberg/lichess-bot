# Module for evaluating a position
import chess

from src.board_representation import BoardRepresentation

def evaluate(board: chess.Board) -> int:
    board_representation = BoardRepresentation(board)

    return board_representation.material_diff()

if __name__ == "__main__":
    board = chess.Board()
    evaluate(board)