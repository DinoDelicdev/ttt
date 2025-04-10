from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        fields = self.board.fields
        # Check rows, columns, and diagonals for a winner
        for row in fields:
            if row[0] == row[1] == row[2]:
                return row[0]
        for col in range(3):
            if fields[0][col] == fields[1][col] == fields[2][col]:
                return fields[0][col]
        if fields[0][0] == fields[1][1] == fields[2][2]:
            return fields[0][0]
        if fields[0][2] == fields[1][1] == fields[2][0]:
            return fields[0][2]
        return None

    def play(self):
        while True:
            self.board.display()
            move = int(input(f"Player {self.current_player}, enter your move: "))
            self.board.add_player_move(move, self.current_player)
            winner = self.check_winner()
            if winner:
                self.board.display()
                print(f"Player {winner} wins!")
                break
            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break
            self.switch_player()