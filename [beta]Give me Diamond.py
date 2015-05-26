def diamond(n):
    if n % 2 == 0 or n < 1:
        return None
    layers = [(' ' * ((n-i)//2) + '*' * i) for i in range(1,n,2)]
    upper = '\n'.join(layers) + '\n'
    center = '*' * n + '\n'
    lower = '\n'.join(reversed(layers)) + '\n'
    return upper + center + lower  

print(diamond(3))    