def check_valid_tr_number(number):
    if len(str(number)) != 11 or any([str(c) not in '0123456789' for c in str(number)]):
        return False
    sum_13579 = sum([int(number[n]) * 7 for n in range(0,9) if n in (0,2,4,6,8)])
    sum_2468 = sum([int(number[n]) for n in range(0,9) if n in (1,3,5,7)])
    if (sum_13579-sum_2468) % 10 != int(number[9]):
        return False
    if sum([int(number[n]) for n in range(10)]) % 10 != int(number[10]):
        return False
    return True


print(check_valid_tr_number('10167994524'))    
print(check_valid_tr_number('36637640050'))