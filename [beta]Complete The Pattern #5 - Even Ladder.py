def pattern(n):
    if n <= 1:
        return ''
    n = n-1 if n %2 != 0 else n
    
    return '\n'.join([str(i) * i for i in range(2,n+1,2)])

for i in range(1,10):
    print(pattern(i))