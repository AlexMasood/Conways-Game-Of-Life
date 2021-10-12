import pygame
from board import Board
import time

class main:
    def __init__(self,pixelSize = 5, dimension = 100):
        pygame.init()
        self.pixelSize = pixelSize
        self.dimension = dimension
        self.setupScreen()
        self.run()

    def setupScreen(self):
        pygame.display.set_mode((self.dimension*self.pixelSize,self.dimension*self.pixelSize))
        self.screen = pygame.display.get_surface()

    def run(self):
        board = Board(self.dimension)
        board.randomBoard()
        loop = True
        while loop:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    loop = False

            self.screen.fill((0,0,0)) 
            board.update(board.boardA,board.boardB)
            img = pygame.surfarray.make_surface(board.boardB)
            img = pygame.transform.scale(img, (self.dimension * self.pixelSize,self.dimension * self.pixelSize))
            self.screen.blit(img,(0,0))
            pygame.display.flip()


            
            self.screen.fill((0,0,0))
            board.update(board.boardB,board.boardA)
            img = pygame.surfarray.make_surface(board.boardA)
            img = pygame.transform.scale(img, (self.dimension * self.pixelSize,self.dimension * self.pixelSize))
            self.screen.blit(img,(0,0))
            pygame.display.flip()

            
        pygame.quit()

if __name__ == "__main__":
    main()
