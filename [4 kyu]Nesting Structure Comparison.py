def same_structure_as(original,other):
    if type(original) in ('str','int') and type(other) in ('str','int'):
        if ''.join(map(str,original)) == ''.join(map(str,other)):
            return True
        if ''.join(map(str,original)) == ''.join(map(str,other))[::-1]:
            return True
        else:
            return  False

    if type(original) != type(other):
        return False

    if len(original) != len(other):
        return False
    for ori,oth in zip(original,other):
        if type(ori) != type(oth):
            return False
        elif type(ori) == type(oth) and isinstance(ori,list):
            if not same_structure_as(ori,oth) or len(ori) != len(oth):
                return False
    return True                


print(same_structure_as([1,[1,1]],[2,[2,2],[2,3]]))
print(same_structure_as([1,'[',']'], ['[',']',1]))
