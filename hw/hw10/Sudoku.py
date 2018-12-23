import numpy as np

class sudoku():
    def __init__(self):
        self.board  = np.zeros((9,9), dtype=int) # start with blank board
        self.__fill_cell(0)
        
    def __fill_cell(self,k):
        if k==81:
            return True      
        i = k // 9
        j = k % 9

        row = set(self.board[i,:])
        column = set(self.board[:,j])
        square = set(self.board[(i//3)*3:(1+i//3)*3,(j//3)*3:(1+j//3)*3].flatten())
        usedNumSet = row.union(column).union(square)
        # pick a number for cell (i,j) from the set of remaining available numbers        
        choices = list(set(range(1,10)).difference(usedNumSet))
        np.random.shuffle(choices)
        for choice in choices:
            self.board[i,j] = choice
            if self.__fill_cell(k+1):
                return True
        self.board[i,j] = 0
        return False
        
    def __fill_free_cell(self,k):
        if k==81:
            self.soution_counter += 1
            print("solution %d :" % (self.soution_counter))
            print(self.puzzel)
            return
        
        i = k // 9
        j = k % 9
        
        if(self.mask[i,j]==1):
            self.__fill_free_cell(k+1)
            return

        row = set(self.puzzel[i,:])
        column = set(self.puzzel[:,j])
        square = set(self.puzzel[(i//3)*3:(1+i//3)*3,(j//3)*3:(1+j//3)*3].flatten())
        usedNumSet = row|column|square
        # pick a number for cell (i,j) from the set of remaining available numbers        
        choices = list(set(range(1,10)) - usedNumSet)

        for choice in choices:
            self.puzzel[i,j] = choice
            self.__fill_free_cell(k+1)
            
        self.puzzel[i,j] = 0
        return
        
    def get_puzzle(self, n=45):
        mask = np.array([0]*n+[1]*(81-n),dtype=int)
        np.random.shuffle(mask)
        self.mask = mask.reshape(9,9)
        self.puzzel = self.mask * self.board
        return self.puzzel

    def get_solution(self):
        return self.board
    
    def get_all_solution(self):
        self.soution_counter = 0
        self.__fill_free_cell(0)
            
mysudoku = sudoku()
print("puzzle:")
print(mysudoku.get_puzzle())

print("solution:")
print(mysudoku.get_solution())

print("all solution:")
mysudoku.get_all_solution()

