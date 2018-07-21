import random

class Matrix:

    matrix=[]
    nrow=0
    ncol=0
    
    def __init__(self,nrow,ncol):
        self.nrow=nrow
        self.ncol=ncol
        self.matrix = [[random.randint(0, 9) for j in range(self.ncol)] for i in range(self.nrow)]
    
    def add(self,b):
        
        if self.nrow !=b.nrow or self.ncol !=b.ncol:
            print('Matrixs\' size should be in the same size')
            
        for i in range(self.nrow) :
            for j in range(self.ncol):
                self.matrix[i][j]=self.matrix[i][j]+b.matrix[i][j]
        return self
    
    def sub(self,b):
        
        if self.nrow !=b.nrow or self.ncol !=b.ncol:
            print('Matrixs\' size should be in the same size')
            
        for i in range(self.nrow) :
            for j in range(self.ncol):
                self.matrix[i][j]=self.matrix[i][j]-b.matrix[i][j]
        return self
    
    def mul(self, b):
        
        if self.nrow !=b.ncol :
            print('')
        
        e=Matrix(b.nrow,self.ncol)
        
        for j in range(self.ncol) :
            for k in range(b.nrow):
                for i in range(self.nrow):
                    e[k][j]+=self.matrix[i][j]*b.matrix[k][i]
        

    def display(self):
        n=self.nrow
        m=self.ncol
        for i in range(n):
            for j in range(m):
                print(self.matrix[i][j],end='  ')
            print(' ')
        

A=Matrix(3,5)
B=Matrix(3,5)
A.display()
B.display()
C=A.add(B)
C.display()
D=A.sub(B)
D.display()
E=A.mul(B)
E.display




   