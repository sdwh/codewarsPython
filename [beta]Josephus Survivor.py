def josephus_survivor(n,k):
    circle = [i for i in range(1,n+1)]
    index = -1
    while circle.count(0) != n-1:
        steps = k
        while steps > 0:
            if index + 1 > n-1:
                index = 0
                steps -= 1
            elif circle[index+1] == 0:
                index += 1
            else:
                index += 1
                steps -= 1
        circle[index] = 0
        print(circle,index)
    for num in circle:
        if num != 0:
            return num
print(josephus_survivor(14,2))

#[1,2,3,4,5,6,7] - initial sequence 3
#[1,2,4,5,6,7] => 3 is counted out 6
#[1,2,4,5,7] => 6 is counted out 9 2
#[1,4,5,7] => 2 is counted out 12 5
#[1,4,5] => 7 is counted out 15 
#[1,4] => 5 is counted out
#[4] => 1 is the last element - the survivor!