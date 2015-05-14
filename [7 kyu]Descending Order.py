def Descending_Order(num):
    return int(''.join(sorted([c for c in str(num)],reverse = True)))

print(Descending_Order(96588989161))

