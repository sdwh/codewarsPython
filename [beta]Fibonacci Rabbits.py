def fib_rabbits(n, b):
    n -= 1
    young,adult = 1,0
    while n > 0:
        young,adult = adult * b , adult + young
        n -= 1
    return young + adult
    

