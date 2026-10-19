def count(k):
    pos = 0
    neg = 0
    nul = 0

    for n in k:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            nul += 1

    return pos, neg, nul

m = [2, 0, -3, 5, 0]
print(count(m))
