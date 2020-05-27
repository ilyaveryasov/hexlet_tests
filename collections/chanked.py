def chuked(n, iterable):
    result =[]
    for i in range(0, len(iterable), n):
        result.append(iterable[i: n + i])
    return result
