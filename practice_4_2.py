# Вводим значения A и B
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Проверяем условие и выводим числа в нужном порядке
if A < B:
    for i in range(A, B + 1):
        print(i, end=' ')
else:
    for i in range(A, B - 1, -1):
        print(i, end=' ')