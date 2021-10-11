import pygame
import numpy as np


def randomBoard(dim):
    boardA = np.random.choice([0,1], dim*dim, p=[0.8, 0.2]).reshape(dim, dim)
    boardB = boardA.copy()
    return boardA, boardB

def update(currentBoard,newBoard):
    dimension = len(currentBoard)
    for row in range(dimension):
        for col in range(dimension):
            total = (currentBoard[row,(col-1)%dimension] + currentBoard[row,(col+1)%dimension] +
                currentBoard[(row-1)%dimension,col] + currentBoard[(row+1)%dimension,col] +
                currentBoard[(row-1)%dimension,(col-1)%dimension] + currentBoard[(row-1)%dimension,(col+1)%dimension] +
                currentBoard[(row+1)%dimension,(col-1)%dimension] + currentBoard[(row+1)%dimension,(col+1)%dimension])
            
            if (currentBoard[row,col] == 1):
                if (total < 2) or (total > 3):
                    newBoard[row,col] = 0
            else:
                if (total == 3):
                    newBoard[row,col] = 1

    return newBoard
boardA,boardB = randomBoard(10)
print(boardA)
print("#####")
boardB = update(boardA,boardB)
print(boardB)
print("#####")
boardA = update(boardB,boardA)
print(boardA)
print("#####")


