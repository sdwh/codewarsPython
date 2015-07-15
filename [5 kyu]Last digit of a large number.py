def last_digit(n1, n2):
    res = {            
            1 : [1],
            2 : [2,4,8,6],
            3 : [3,9,7,1],
            4 : [4,6],
            5 : [5],
            6 : [6],
            7 : [7,9,3,1],
            8 : [8,4,2,6],
            9 : [9,1],
            0 : [0]
    }
    n1 %= 10
    if n2 == 0:
        return 1
    elif n1 in (1,5,6,0):
        return n1
    else:
        return res[n1][n2%len(res[n1]) - 1]

for i in range(0,5):
    print(last_digit(34,i))    