def pattern(n):
    string = ''
    res = []
    for i in range(n,0,-1):
        string += str(i)
        res.append(string)
    return '\n'.join(res)
        


for i in (13,):
    print(pattern(i))    