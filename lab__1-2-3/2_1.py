import math 

x = float(3.981 * 10 **(-2))
y = float(-1.625 * 10 ** 3)
z = float(0.512)

s = 2 ** (-x) * (pow((x + (pow(abs(y), 1/4))), 1/2) * (pow((math.exp((x-1)/(math.sin(z)))),1/3)))
print(s)