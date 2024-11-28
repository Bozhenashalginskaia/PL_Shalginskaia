
matrix = [
    [1, 2, 3, 4],
    [3, 7, 8, 6],
    [8, 9, 7, 6]
]

def product_of_column(matrix, col_index):
    product = 1
    for row in matrix:
        product *= row[col_index]
    return product

min_product = float('inf')
min_index = -1

for col in range(len(matrix[0])):
    col_product = product_of_column(matrix, col)
    if col_product < min_product:
        min_product = col_product
        min_index = col

if 0 <= min_index < len(matrix[0]) - 1:
    for row in matrix:
        row[min_index], row[min_index + 1] = row[min_index + 1], row[min_index]

for row in matrix:
    print(row)
