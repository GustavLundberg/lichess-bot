import chess

class BoardRepresentation():
    """Representation of the board."""

    def __init__(self, board: chess.Board) -> None:
        self.representation = BoardRepresentation.from_board(board)

    @staticmethod
    def from_board(board: chess.Board):
        """"""
        return [[el if el != "." else None for el in row.split(" ")] for row in board.__str__().split("\n")]
    
    def material_diff(self):
        """"""
        white_count = 0
        black_count = 0

        for row in self.representation:
            for el in row:

                if el == "p":
                    black_count += 1

                elif el == "r":
                    black_count += 5

                elif el == "n":
                    black_count += 3
                
                elif el == "b":
                    black_count += 3
                
                elif el == "q":
                    black_count += 9

                elif el == "P":
                    white_count += 1

                elif el == "R":
                    white_count += 5

                elif el == "N":
                    white_count += 3
                
                elif el == "B":
                    white_count += 3
                
                elif el == "Q":
                    white_count += 9
        
        return white_count - black_count



if __name__ == "__main__":
    board = chess.Board("rnb1kbnr/pppp1ppp/8/4p3/8/8/PPPP1PPP/2BQKBNR w kq e6 0 1")

    board_representation = BoardRepresentation(board)
    print(board_representation.representation)
    print(board_representation.material_diff())