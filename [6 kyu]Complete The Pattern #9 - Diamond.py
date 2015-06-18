def pattern(n):
    res = []
    spaces = (2 * n) - 1
    for i in range(1,n+1):
    	term = list(range(1,i+1)) + list(range(i-1,0,-1))
    	term = [t%10 for t in term]
    	term = [' '] * int(((spaces - len(term))/2)) + term + [' '] * int(((spaces - len(term))/2))
    	term = ''.join(map(str,term))
    	res.append(term)
    res += res[-2::-1]
    return '\n'.join(res)


print(pattern(27))    
