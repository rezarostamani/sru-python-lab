import pygame,sys
from pygame.locals import *

WX = 500
WY = WX
L = WX / 8

WHITE = pygame.Color(0xFF,0xFF,0xFF)
BLACK = pygame.Color(0x00,0x00,0x00)
RED = pygame.Color(0xFF,0x00,0x00)
GREEN = pygame.Color(0x00,0xFF,0x00)
BLUE = pygame.Color(0x00,0x00,0xFF)


class EightQueen:
    def __init__(self):
        self.board = [-1]*8
        self.case = 0
        self.row = 0
        
    def checkBoard(self):
        if self.board.count(self.board[self.row])>1:
            return False
        for i in range(self.row):
            if abs(self.board[i]-self.board[self.row])==abs(self.row-i):
                return False
        return True
              
    def reset(self):
        self.__init__()

    def getNextBoard(self):
        while self.row >= 0:
            self.board[self.row] += 1
            if self.board[self.row]>7:
                self.board[self.row]=-1
                self.row -= 1
                continue    
            if self.checkBoard():
                if self.row == 7:
                    self.case += 1
                    print(self.board)
                    return self.board
                else:
                    self.row += 1
        else:
            return None

def main():
    #Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((WX, WY), 0, 32)
    screen.fill((0xFF,0xFF,0xFF))
    pygame.display.set_caption('Eight Queen')

    fpsClock = pygame.time.Clock()  
    
    queenpic = pygame.image.load("queen.png")
    queenpic = pygame.transform.scale(queenpic,(int(L), int(L)))
    eq = EightQueen()
    board  = eq.getNextBoard()
    pygame.key.set_repeat(1, 1)
    
    while True: # main game loop
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    board  = eq.getNextBoard()
                    
                if event.key == K_ESCAPE:
                    eq.reset()
                    board  = eq.getNextBoard()
                
        if board:            
            #Draw Everything
            screen.fill((0xFF,0xFF,0xFF))
            for i in range(8):
                for j in range(8):
                    pygame.draw.rect(screen,BLACK if (i+j)%2 else WHITE,(i*L,j*L,L,L))
                screen.blit(queenpic,(i*L, board[i]*L))
                
            fpsClock.tick(10)            
            pygame.display.update()        


        
#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()

        

