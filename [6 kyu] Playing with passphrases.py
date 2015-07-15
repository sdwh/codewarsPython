def play_pass(s, n):
    res = ''
    for c in map(ord,s):
        if c in range(65,91):
            res += chr((((c-65) + n) % 26) + 65)
        elif c in range(97,123):
            res += chr((((c-97) + n) % 26) + 97)
        elif c in range(48,58):
            res += str (abs(9 - int(chr(c))))
        else:
            res += str(chr(c))
    res = ''.join([res[i].upper() if i % 2 == 0 else res[i].lower() for i in range(len(res))])
    return res[::-1]