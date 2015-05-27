def tickets(people):
    cashier = {100:0,50:0,25:0}
    for pay in people:
        if pay == 25:
            cashier[25] += 1
        elif pay == 50:
            if cashier[25] == 0:
                return 'NO'
            cashier[50] += 1
            cashier[25] -= 1
        else:
            cashier[100] += 1
            if cashier[50] >= 1 and cashier[25] >= 1:
                cashier[50] -= 1
                cashier[25] -= 1
            elif cashier[25] >= 3:
                cashier[25] -= 3
            else:
                return 'NO'
    return 'YES'


print(tickets([25,25,25,100,25,50]))    