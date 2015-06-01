def is_merge(s, part1, part2):
    part1 = list(part1)
    part2 = list(part2)
    for i in range(len(s)):
        if s[i] == part1[0]:
            print(part1)
            print(part1.pop())


print(is_merge('codewars', 'cod', 'ewars'))
print(is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am'))

        #if s[i] in part1 and s[i] in part2:
            #if is_merge(''.join(s[i+1:]),part1.pop()[::-1],part2[::-1]):
            #    return True
            #return False