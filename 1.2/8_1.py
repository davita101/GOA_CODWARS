def divisible_by(n, d):
    arr = []
    for i in n:
        if i % d == 0:
            arr.append(i)
    return arr