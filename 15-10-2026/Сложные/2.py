def rotate(numbers, k):
    if not numbers or k == 0:
        return list(numbers)

    n = len(numbers)
    k = k % n

    if k == 0:
        return list(numbers)

    return numbers[-k:] + numbers[:-k]

# проверки
print(rotate([10, 20, 30, 40, 50], 2)) # [40, 50, 10, 20, 30]
print(rotate([10, 20, 30, 40, 50], -1)) # [20, 30, 40, 50, 10]
print(rotate([1, 2, 3], 8)) # [2, 3, 1]