n = int(input())

b = input()

c = input()

d = input()

count = 0

for i in range(100, n + 1):
    f = str(i)
    if n in f and d in f:
        count += 1

print(count)

# a, b, c
# [100, N] (210 < N < 231)