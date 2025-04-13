import random
from board import Board
from ai_player import AI_Player
from winner_checker import WinnerChecker
from prompt_validator import PromptValidator

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = random.choice(["X", "O"])
        self.ai = AI_Player(self.board)
        self.winner_checker = WinnerChecker(self.board)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        # self.current_player = "O" if self.board.get_num_of_moves() % 2 == 1 else "X"


    def play(self):
        while True:
            self.board.display()
            if (self.current_player == "X"):
                while True:  
                    user_input = input(f"Player {self.current_player}, enter your move: ")
                    if PromptValidator.is_valid_input(user_input):
                        move = int(user_input)
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 9.")
            else:
                move = self.ai.make_move()
                
            self.board.add_player_move(move, self.current_player)
            if self.board.get_num_of_moves() >= 5:
                print("Now I got started")
                winner = self.winner_checker.check_winner()
                if winner:
                    self.board.display()
                    print(f"Player {winner} wins!")
                    break
                if self.board.is_full():
                    self.board.display()
                    print("It's a draw!")
                    break
            self.switch_player()