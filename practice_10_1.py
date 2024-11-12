vvod_filename = "Шалгинская_УБ41_vvod.txt"
vivod_filename = "Шалгинская_УБ41_vivod.txt"

with open(vvod_filename, 'r') as file:
    matrix = []
    for line in file:
        row = list(map(int, line.strip('[], \n').split(',')))
        matrix.append(row)

min = matrix[0][0]
index = 0

for i in range (len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < min:
            min = matrix[i][j]
            index = i

result = sum(matrix[min])
print("Сумма элементов с наименьшим элементом", result)

with open(vivod_filename, 'w') as file:
    file.write(str(result))

