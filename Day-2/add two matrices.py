import numpy as np
def create_matrix():
    rows= int(input("Enter the number of rows:"))
    cols= int(input("Enter the number of columns:"))
    matrix=[]
    for i in range(rows):
        rows=[]
        for j in range(cols):
            value=int(input(f"Enter the value of the matrix at {i+1},{j+1}:"))
            rows.append(value)
        matrix.append(rows)
    return matrix

def addition(mat1,mat2):
    sum= np.add(mat1,mat2)
    return sum

def print_max(matrix):
    print("The result is:")
    for row in matrix:
        print("".join(map(str,row)))

print("Enter the 1st matrix..")
mat1=create_matrix()
print("Enter the 2nd matrix...")
mat2= create_matrix()
Sum=addition(mat1,mat2)
print_max(Sum)