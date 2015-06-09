def pattern(n):
    if n < 1:
        return ''
    res = '1'
    for i in range(2,n+1):
        res += '\n' + str(i) * i
    return res
