
s = str(input())

def cont(s) : 
    c = s.split()
    c.reverse()
    res = " ".join(c)
    return res
    

print(cont(s))

