# Use a list literal to create a nested list
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# The length of the list: The number of elements
n = len(mat)

# Iterate of the rows: i represents the row number
for i in range(n):
    # Iterate over the columns: j represents the column number
    for j in range(n):
        # Change the value of the element on position i, j in mat
        mat[i][j] *= 2
        # Print the element on the given position, end with a space
        print(f'{mat[i][j]:2}', end=' ')
    # End the line
    print()

print()

# For each row in the matrix: For each list in the outer list
for row in mat:
    # For each element in the row: For each element in the inner list
    for item in row:
        # Print the element, end with a space
        print(f'{item:2}', end=' ')
    # End the line
    print()

print()

# Create an empty list, to contain a copy of the nested list
mat2 = []
# Iterate of the rows: i represents the row number
for i in range(n):
    # Add a new row to the matrix mat2
    mat2.append([])
    # Iterate over the columns: j represents the column number
    for j in range(n):
        # Retrieve the element at position i, j in mat
        item = mat[i][j]
        # Add the element to the current row of the new matrix mat2
        mat2[i].append(item)

print(mat2)