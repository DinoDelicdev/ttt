from winner_checker import WinnerChecker

class WinFinder:
    def __init__(self, board):
        self.board = board
        self.winner_checker = WinnerChecker(board)

    def find_winning_move(self, player):
        for move in self.board.get_available_fields().keys():
            i, j = self.board.index_map[move]
            original_value = self.board.fields[i][j]
            self.board.fields[i][j] = player

            if self.winner_checker.check_winner() == player:
                self.board.fields[i][j] = original_value
                return move

            
            self.board.fields[i][j] = original_value

        return None  