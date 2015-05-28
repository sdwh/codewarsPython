def get_num(n):
    return sum([2 if c == '8' else 1 for c in str(n) if c in ('0','6','8','9')])
        
print(get_num(300))