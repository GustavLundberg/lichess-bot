import chess

class BoardRepresentation():
    """Representation of the board."""

    def __init__(self, board: chess.Board) -> None:
        self.representation = BoardRepresentation.from_board(board)

    @staticmethod
    def from_board(board: chess.Board):
        return [[el if el != "." else None for el in row.split(" ")] for row in board.__str__().split("\n")]


if __name__ == "__main__":
    board = chess.Board()
    board_representation = BoardRepresentation(board)
    print(board_representation.representation)