class Board():
  def __init__(self):
    self.__num_of_moves = 0
    self.fields = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    self.index_map = {cell: (i, j) for i, row in enumerate(self.fields) for j, cell in enumerate(row)}

  def display(self):
    
    for i, row in enumerate(self.fields):
        for ii, cell in enumerate(row):
            if ii == len(row) - 1: 
                print(cell, end=" ")
            else:
                print(cell, end=" | ")
        if not i == len(self.fields) - 1:
          print("\n----------")
        else:
           print("\n")

  
  def add_player_move(self, num, char):
     if num in self.index_map:  
        i, j = self.index_map[num]  
        self.fields[i][j] = char  
        del self.index_map[num]  
        self.__num_of_moves += 1
     else:
        print(f"Number {num} not found on the board.")
  
  def get_num_of_moves(self):
     return self.__num_of_moves
  
  def is_full(self):
        return len(self.index_map) == 0
  
  def get_available_fields(self):
     return self.index_map
  
  def get_available_corners(self):
     return list(filter(lambda move: move in [1, 3, 7, 9] ,list(self.index_map.keys())))
  
  def get_available_center(self):
     return list(filter(lambda move: move in [5] ,list(self.index_map.keys())))