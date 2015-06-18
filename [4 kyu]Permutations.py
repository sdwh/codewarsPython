import itertools
def permutations(string):
    return sorted([''.join(p) for p in set(itertools.permutations(string,len(string)))])

print(permutations('aabb'))    