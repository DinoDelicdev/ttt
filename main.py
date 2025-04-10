# import sys

# def delete_multiple_lines(n=6):
#     """Delete the last line in the STDOUT."""
#     for _ in range(n):
#         sys.stdout.write("\x1b[1A")  # cursor up one line
#         sys.stdout.write("\x1b[2K") 

# from board import Board

# empty_board = Board()

# # print(empty_board.fields[0][1])
# empty_board.display()


# empty_board.add_player_move(4, "X")
# delete_multiple_lines()
# empty_board.display()

# empty_board.add_player_move(5, "O")

# delete_multiple_lines()
# empty_board.display()

# print(empty_board.get_num_of_moves())


# empty_board.add_player_move(1, "O")
# empty_board.display()

# print(empty_board.get_num_of_moves())

from game import Game

if __name__ == "__main__":
    game = Game()
    game.play()