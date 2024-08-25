class Matrix:
    def getValues(self,rows,cols):
        self.M=[]
        for i in range(rows):
            C=[]
            for j in range(cols):
                C.append(int(input("Enter values[{}][{}]:".format(i,j))))
            self.M.append(C)

    def putMatrix(self):
        for r in self.M:
            for c in r:
                print(c,end='')
            print()
    
    def add(self,other):
        R=Matrix()
        R.M=[]
        for i in range(len(self.M)):
            C=[]
            for j in range(len(self.M[i])):
                C.append(self.M[i][j]+other.M[i][j])
            R.M.append(C)
        return R
    

print("Matrix 1 :")
mat1=Matrix()
mat1.getValues(3,3)
mat1.putMatrix()

print("Matrix 2 :")
mat2=Matrix()
mat2.getValues(3,3)
mat2.putMatrix()

mat3=mat1.add(mat2)
print("Addition Matrix:")
mat3.putMatrix()



