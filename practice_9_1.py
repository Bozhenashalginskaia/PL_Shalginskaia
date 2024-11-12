l = []

def sum_number(n):
    if (n == 0):
        return 1
    a = n % 10
    l.append(a)
    sum_number(n // 10)
b = int(input("Введите число: "))
sum_number(b)
print(l)
print(sum(l)) 
    