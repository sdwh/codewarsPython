def pattern(n):
    string = [str(i) for i in range(1,n+1)]
    return '\n'.join([''.join(lst) for lst in [string[i:] for i in range(n)]])

for i in (0,1,2,3,4,5):
    print(pattern(i))    