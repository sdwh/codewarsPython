def unique_in_order(iterable):
    res = []
    for c in iterable:
        if len(res) == 0 or res[-1] != c:
            res.append(c)
    return res