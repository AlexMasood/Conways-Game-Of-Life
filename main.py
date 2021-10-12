import pygame
from board import Board

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

            board.update(board.boardA,board.boardB)
            #create and resize image of the board
            img = pygame.surfarray.make_surface(board.boardB)
            img = pygame.transform.scale(img, (self.dimension * self.pixelSize,self.dimension * self.pixelSize))

            #draw to the screen
            self.screen.fill((0,0,0)) 
            self.screen.blit(img,(0,0))
            pygame.display.flip()

            #swap boards a and b
            board.boardA,board.boardB = board.boardB,board.boardA
        pygame.quit()

if __name__ == "__main__":
    main()
