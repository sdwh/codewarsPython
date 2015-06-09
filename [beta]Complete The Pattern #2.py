def pattern(n):
    string = ''.join([str(i) for i in range (1,n+1)][::-1])
    res = ''
    for i in range(1,n+1):
        res += '\n' if len(res) > 0 else ''
        res += string
        string = string[:-1] if len(str(i)) == 1 else string[:-2]
    return res
        


for i in (13,):
    print(pattern(i))    