def reverse_it(data):
    if isinstance(data,bool):
        return data
    elif isinstance(data,int):
        return int(str(data)[::-1])
    elif isinstance(data,str):
        return data[::-1]
    elif isinstance(data,float):
        return float(str(data)[::-1])

    else:
        return data

    