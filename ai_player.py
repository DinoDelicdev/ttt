import random
from win_finder import WinFinder

class AI_Player:
  def __init__(self, board):
    self.board = board
    self.win_finder = WinFinder(self.board)

  def __make_side_move(self):
    return list(self.board.get_available_fields().keys())
  
  def __make_corner_move(self):
    return self.board.get_available_corners()
  
  def __make_center_move(self):
    return self.board.get_available_center()
  
  def __make_lesser_move(self):
    if len(self.__make_corner_move()):
      return random.choice(self.__make_corner_move())
    elif len(self.__make_center_move()):
      return self.__make_center_move()[0]
    else:
      return random.choice(self.__make_side_move())
    
  def __make_major_move(self):
    if (self.win_finder.find_winning_move("O")):
      return self.win_finder.find_winning_move("O")
    elif (self.win_finder.find_winning_move("X")):
      return self.win_finder.find_winning_move("X")
    else:
      return self.__make_lesser_move()

  
  def make_move(self):
    if self.board.get_num_of_moves() < 3:
      return self.__make_lesser_move() 
    else:
      return self.__make_major_move()
      
  

    