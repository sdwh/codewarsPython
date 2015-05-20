def is_vampirenumber(multiplicand1, multiplicand2):
    if multiplicand1 == None or multiplicand2 == None:
        return False
    return sorted(str(multiplicand1 * multiplicand2)) == sorted(str(multiplicand1)+str(multiplicand2))

