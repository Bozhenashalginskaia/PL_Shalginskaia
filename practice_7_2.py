
s = str(input())

def cont(s) : 
    # разделение на слова
    c = s.split()
    #наоборот
    c.reverse()
    # объединение
    res = " ".join(c)
    return res
    

print(cont(s))

