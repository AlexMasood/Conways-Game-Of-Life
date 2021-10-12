import numpy as np

class Board:
    def __init__(self,dimension):
        self.dimensions = dimension
        #2 boards are used to prevent repeated creation and deletion
        self.boardA = np.empty([dimension,dimension])
        self.boardB = np.empty([dimension,dimension])
        
    def randomBoard(self):
        self.boardA = np.random.choice([0,1], self.dimensions*self.dimensions, p=[0.8, 0.2]).reshape(self.dimensions, self.dimensions)
    

    def update(self,currentBoard,newBoard):
        dimension = self.dimensions
        for row in range(dimension):
            for col in range(dimension):
                #get neighbours
                total = (currentBoard[row,(col-1)%dimension] + currentBoard[row,(col+1)%dimension] +
                    currentBoard[(row-1)%dimension,col] + currentBoard[(row+1)%dimension,col] +
                    currentBoard[(row-1)%dimension,(col-1)%dimension] + currentBoard[(row-1)%dimension,(col+1)%dimension] +
                    currentBoard[(row+1)%dimension,(col-1)%dimension] + currentBoard[(row+1)%dimension,(col+1)%dimension])
                #applying the rules
                if (currentBoard[row,col] == 1):
                    if (total < 2) or (total > 3):
                        newBoard[row,col] = 0
                    else:
                        newBoard[row,col] = 1
                else:
                    if (total == 3):
                        newBoard[row,col] = 1
                    else:
                        newBoard[row,col] = 0
