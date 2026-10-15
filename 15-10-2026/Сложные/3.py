def compress(numbers):
    if not numbers: return []
    res = [[numbers[0], 0]]
    for n in numbers:
        if n == res[-1][0]:
            res[-1][1] += 1
        else:
            res.append([n, 1])
    return res

def decompress(groups):
    return [num for num, count in groups for _ in range(count)]

numbers = [5, 5, 5, 2, 2, 5, 8, 8]

print(compress(numbers)) # [[5, 3], [2, 2], [5, 1], [8, 2]]
print(decompress(compress(numbers))) # [5, 5, 5, 2, 2, 5, 8, 8]