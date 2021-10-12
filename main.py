import pygame
from board import Board
import time

class main:
    def __init__(self,pixelSize = 10, dimension = 100):
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
            board.boardB = board.update(board.boardA,board.boardB)
            img = pygame.surfarray.make_surface(board.boardB)
            img = pygame.transform.scale(img, (self.dimension * self.pixelSize,self.dimension * self.pixelSize))
            self.screen.blit(img,(0,0))
            #self.drawBoard(board.boardB)
            pygame.display.flip()
            time.sleep(0.5)


            self.screen.fill((0,0,0))
            board.boardA = board.update(board.boardB,board.boardA)
            img = pygame.surfarray.make_surface(board.boardA)
            img = pygame.transform.scale(img, (self.dimension * self.pixelSize,self.dimension * self.pixelSize))
            self.screen.blit(img,(0,0))
            #self.drawBoard(board.boardA)
            pygame.display.flip()
            time.sleep(0.5)
        pygame.quit()

if __name__ == "__main__":
    main()
