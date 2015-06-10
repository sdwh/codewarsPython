from functools import reduce

def fromNb2Str(n, modsys):
    prime = [i for num in modsys for i in range(2,num+1) if num%i == 0]
    for p in prime:
        if prime.count(p) > 1:
            return 'Not applicable'
    
    if reduce(lambda x,y:x*y, modsys) < n:
        return 'Not applicable'
    return '-' + '--'.join([str(n%num) for num in modsys]) + '-'

print(fromNb2Str(187,[8,7,5,3]))
print(fromNb2Str(15,[8,6,5,3]))