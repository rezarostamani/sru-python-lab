import numpy as np

class maze():
    def __init__(self,m,p,k):
        self.m = m
        self.p = p
        puzzel = np.array([1]*k+[0]*(m*p-k), dtype=int)
        np.random.shuffle(puzzel)
        self.puzzel = puzzel.reshape(m,p)
        self.puzzel[0,0] = 0
        self.puzzel[m-1,p-1] = 0
        
    def __find_way(self,i,j):
        m = self.m
        p = self.p
        
        if (i >= m) or (j >= p) or (i < 0) or (j < 0) or (self.puzzel[i,j]==1) or (self.puzzel[i,j]==2):
            return False
        
        if (i == m-1) and (j == p-1):
            print("the solution:")
            print(self.puzzel)
            return True     
      
        directions  = ((-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1))

        self.puzzel[i,j] = 2
        
        for nextdir in directions:
            if self.__find_way(i + nextdir[0], j + nextdir[1]):
                return True
            
        self.puzzel[i,j] = 0
        
        return False
        
    def get_puzzle(self):
        return self.puzzel
    
    def get_solution(self):
        if not self.__find_way(0,0):
            print("no solution")
            
mymaze = maze(7,10,35)
print("puzzle:")
print(mymaze.get_puzzle())

mymaze.get_solution()

