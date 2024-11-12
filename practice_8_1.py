# сумма элементов где расположен наименьший элемент строки

matr = [ 
    [5,4,9],
    [1,2,3],
    [9,8,7]
]

min = matr[0][0]
index = 0

for i in range (len(matr)):
    for j in range(len(matr[i])):
        if matr[i][j] < min:
            min = matr[i][j]
            index = i

result = sum(matr[min])
print("Сумма элементов с наименьшим элементом", result)