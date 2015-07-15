def pattern(n):
    if n <= 0:
        return ''
    if n == 1:
        return '1'
    res = []
    pattern = [' '] * ( 2 * n -1)
    for i in range(1,n):
        temp = pattern[:]
        temp[i-1] = temp[-i] = str(i%10)
        res.append(''.join(temp))
    pattern[n-1] = str(n%10)
    res.append(''.join(pattern))
    res += res[n-2::-1]    
    return '\n'.join(res)

print(pattern(1))