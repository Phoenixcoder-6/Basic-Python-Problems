def create_matrix(rows, cols):
    matrix=[]
    for i in range(rows):
        row= list(map(int,input(f"Enter the number of row {i+1} separated by spaces:").split()))
        while len(row)!= cols:
            print(f"Please enter exactly {cols} elements.")
            row = list(map(int, input(f"Re-enter the elements of row {i + 1} separated by spaces: ").split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Main program
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = create_matrix(rows, cols)

print("The matrix is:")
print_matrix(matrix)
