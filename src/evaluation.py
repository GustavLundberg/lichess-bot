# Module for evaluating a position
import chess

from board_representation import BoardRepresentation

def Evaluate(board: chess.Board) -> int:
    board_representation = BoardRepresentation(board)

    return board_representation.material_diff()

if __name__ == "__main__":
    board = chess.Board()
    Evaluate(board)