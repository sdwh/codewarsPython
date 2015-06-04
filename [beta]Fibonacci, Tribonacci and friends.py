def Xbonacci(signature,n):
    digit = -len(signature)
    while len(signature) < n:
        signature.append(sum(signature[digit:]))
    return signature if n >= len(signature) else signature[:n]


