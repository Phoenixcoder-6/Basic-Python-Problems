def create_matrix():
    rows= int(input("Enter the number of rows:"))
    cols= int(input("Enter the number of columns:"))

    matrix=[]

    for i in range(rows):
        rows=[]
        for j in range(cols):
            value= int(input(f"Enter the values of the position {i+1},{j+1}:"))
            rows.append(value)
        matrix.append(rows)
    return matrix

def print_nicely(matrix):
    print("The given matrix is:")
    for rows in matrix:
        print("".join(map(str,rows)))


matrix= create_matrix()
print_nicely(matrix)


