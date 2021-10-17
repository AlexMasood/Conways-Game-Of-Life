import pygame
from pygame.constants import KEYDOWN
from board import Board
import numpy
class main:
    def __init__(self, dimension = 100, colour = True):
        pygame.init()
        self.pixelSize = int(1000/dimension)
        self.dimension = dimension
        self.setupScreen()
        self.run(colour)

    def setupScreen(self):
        pygame.display.set_mode((self.dimension*self.pixelSize,self.dimension*self.pixelSize))
        self.screen = pygame.display.get_surface()

    def run(self,colour):
        board = Board(self.dimension)
        board.randomBoard()
        loop = True
        update = True
        while loop:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    loop = False
                if (event.type == KEYDOWN):
                    if(pygame.key.get_pressed()[pygame.K_SPACE]):
                        update = not update
                    if(pygame.key.get_pressed()[pygame.K_RETURN]):
                        board.resetBoard()
                    if(pygame.key.get_pressed()[pygame.K_r]):
                        board.randomBoard()
                    if(pygame.key.get_pressed()[pygame.K_s]):
                        board.saveBoard()
                    if(pygame.key.get_pressed()[pygame.K_o]):
                        board.loadBoard()
                        #calculate dimensions and pixelSize in case loaded in board has different dimensions
                        self.dimension = board.dimensions
                        self.pixelSize = int(1000/self.dimension)
                    if(pygame.key.get_pressed()[pygame.K_c]):
                        colour = not colour
                    if(pygame.key.get_pressed()[pygame.K_n]):
                        update = False
                        board.update(board.boardA,board.boardB)
                        board.boardA,board.boardB = board.boardB,board.boardA

                if(pygame.mouse.get_pressed()[0]):#left
                    pos = pygame.mouse.get_pos()
                    board.boardA[int(pos[0]/self.pixelSize)][int(pos[1]/self.pixelSize)] = 1
                    board.colourBoard[int(pos[0]/self.pixelSize)][int(pos[1]/self.pixelSize)] = 1

                if(pygame.mouse.get_pressed()[2]):#right
                    pos = pygame.mouse.get_pos()
                    board.boardA[int(pos[0]/self.pixelSize)][int(pos[1]/self.pixelSize)] = 0
                    board.colourBoard[int(pos[0]/self.pixelSize)][int(pos[1]/self.pixelSize)] = 0

            
            #create and resize image of the board
            if(colour == True):
                img = pygame.surfarray.make_surface(board.colourBoard)
                img = pygame.transform.scale(img, (self.dimension * self.pixelSize,self.dimension * self.pixelSize))
            else:
                img = pygame.surfarray.make_surface(board.boardA)
                img = pygame.transform.scale(img, (self.dimension * self.pixelSize,self.dimension * self.pixelSize))

            #draw to the screen
            self.screen.fill((0,0,0)) 
            self.screen.blit(img,(0,0))
            pygame.display.flip()

            if(update):
                board.update(board.boardA,board.boardB)
                #swap boards a and b
                board.boardA,board.boardB = board.boardB,board.boardA
        pygame.quit()

if __name__ == "__main__":
    main()
