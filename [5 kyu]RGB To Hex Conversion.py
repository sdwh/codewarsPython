def rgb(r, g, b):
    r,g,b = [element if element <= 255 else 255 for element in (r,g,b)]
    r,g,b = [element if element >= 0 else 0 for element in (r,g,b)]
    return ''.join([hex(element)[2:].upper().zfill(2) for element in (r,g,b)])

print(rgb(255,255,300))
print(rgb(1,2,3))
print(rgb(0,0,0))