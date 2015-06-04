import string
def caesar(s, shift):
    transDict = {}
    alpha = string.ascii_lowercase
    alphaTrans = alpha[shift:] + alpha[:shift]
    for key,value in zip(string.ascii_lowercase,alphaTrans):
        transDict[key] = value
        transDict[key.upper()] = value.upper()

    return ''.join([transDict[c] if c in transDict else c for c in s])








