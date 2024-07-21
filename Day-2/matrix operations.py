import numpy as np
print("mat1...")
mat1= np.matrix("10,20,30; 40,50,60; 70,80,90")
print(mat1)
print("mat2...")
mat2= np.matrix("30,40,50; 60,70,80 ; 20,40,60 ")
print(mat2)
#adding matrices
print("mat1+mat2...")
print(np.add(mat1,mat2))
print()
#subtract matrices
print("mat1-mat2...")
print(np.subtract(mat1,mat2))
print()
#multiplication of matrices
print("mat1 * mat2...")
print(np.multiply(mat1,mat2))
print()
#division of matrices
print("mat1/mat2...")
print(np.divide(mat1,mat2))
print()
#producting of matrices
print("mat1 dot mat2...")
print(np.dot(mat1,mat2))
print()
# Square root of matrices
print(" sqrt mat1...")
print(np.sqrt(mat1))
print()
# Square root of matrix elements
print("np.sqrt(mat2)...")
print(np.sqrt(mat2))
print()

