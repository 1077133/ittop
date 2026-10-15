def window_sums(numbers, k):
    if k <= 0 or k > len(numbers):
        return []

    sums = [sum(numbers[:k])]
    for i in range(len(numbers) - k):
        sums.append(sums[-1] + numbers[i + k] - numbers[i])
    return sums

# проверка
print(window_sums([4, 1, 7, 2, 6], 3)) # [12, 10, 15]