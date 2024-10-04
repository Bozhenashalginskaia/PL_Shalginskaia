lst = [10,50,20,40,9,8,2,9,10,36,22,24,25,55,34]

print([0 if i <= 10 else 1 if i >= 20 else i for i in lst])

# x < 10 (0)
# x > 20 (1)