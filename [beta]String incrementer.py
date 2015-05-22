import re
def increment_string(strng):
    strMatch = re.match(r'([\w]*)(\d*)',strng)
    stringPart,numberPart = strMatch.group(1),strMatch.group(2)
    number = re.match(r'0*(\d*)',numberPart).group(1)
    number = 1 if len(number) == 0 else int(number) + 1
    if len(str(number)) >= len(numberPart):
        number = number
    else :
        number = ('0' * (len(numberPart) - len(str(number)))) + str(number)
    return stringPart + str(number)
    


print(increment_string('foobar123'))
print(increment_string('foobar0056'))
print(increment_string('foobar'))
print(increment_string('035'))
print(increment_string(''))
print(increment_string('p)L2_9:0R[800755806{OtCsowX8847280959000119'))