def dig_pow(n, p):
    total = sum([(int(d)**power) for power,d in enumerate([d for d in str(n)],p)])
    return -1 if total%n != 0 else int(total/n)

print(dig_pow(46288, 3))