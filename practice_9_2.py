
i = 2

def recursion(n, i=2):
    if n < 2: 
        return "NO"
    elif n == 2:
        return "YES"
    elif n % 1 == 0:
        return "NO"
    elif i < n // 2:
        return recursion(n, i + 1)
    else:
        return "YES"
    
print(recursion(18))



