vvod_filename = "Шалгинская_УБ41_vvod_2.txt"
vivod_filename = "Шалгинская_УБ41_vivod_2.txt"

with open(vvod_filename, 'r') as file:
    matrix = []
    for line in file:
        row = list(map(int, line.strip('[], \n').split(',')))
        matrix.append(row)


def column_matrix(matrix, index_col):
    for i in matrix:
        if abs(i[index_col]) > 10:
            return False
        return True
    
def product_column(matrix, index_col):
    product = 1
    for i in matrix:
        product *= i[index_col]
    return product

min = float('inf') 
#указывает бесконечность
min_index = -1

number_col = len(matrix[0])

for col in range(number_col):
    if column_matrix(matrix, col):
        column_prod = product_column(matrix, col)
        if column_prod < min:
            min = column_prod
            min_index = col

if min_index != -1 and min_index < number_col - 1:
    for i in matrix:
        i[min_index], i[min_index + 1] = i[min_index + 1], i[min_index]


for i in matrix:
    print(i)


with open(vivod_filename, 'w') as file:
    for i in matrix:
        file.write (','.join(map(str, i)) + '\n')