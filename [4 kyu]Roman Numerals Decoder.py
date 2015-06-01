def solution(roman):
    trans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    signToValue = [trans[c] for c in roman]
    values = 0
    current = 0
    for v in signToValue[::-1]:
        values += v if v >= current else -v
        current = v
    return values

print(solution('XX'))    