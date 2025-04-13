class WinnerChecker:
    def __init__(self, board):
        self.board = board

    def check_winner(self):
        fields = self.board.fields
        # Check rows
        for row in fields:
            if row[0] == row[1] == row[2]:
                return row[0]
        # Check columns
        for col in range(3):
            if fields[0][col] == fields[1][col] == fields[2][col]:
                return fields[0][col]
        # Check diagonals
        if fields[0][0] == fields[1][1] == fields[2][2]:
            return fields[0][0]
        if fields[0][2] == fields[1][1] == fields[2][0]:
            return fields[0][2]
        return None