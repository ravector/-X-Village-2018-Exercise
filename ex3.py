class Map :

    map=[]
    boader=0

    def __init__(self,n,p):
        self.boader=n
        
        for i in range(0,n):
            row=[]
            for j in range(0,n):
                row.append('*')

            self.map.append(row)

        if p==1:

            n=int(self.boader/2)-1

            for i in range(n,n+3):
                self.map[n][i]='0'
            self.map[n+1][n]='0'
            self.map[n+2][n+1]='0'

    def display(self):

        n=self.boader

        for i in range(0,n):
            for j in range(0,n):
                print(self.map[i][j],end=" ")
            print(' ')


a=int(input('n='))      
p=int(input('p='))
x= Map(a,p)
x.display()