def max_sum_segment(numbers):
    if not numbers: return [], 0

    max_sum = current_sum = numbers[0]
    start = best_start = 0
    best_end = 1

    for i in range(1, len(numbers)):
        if numbers[i] > current_sum + numbers[i]:
            current_sum = numbers[i]
            start = i
        else:
            current_sum += numbers[i]

        is_better = current_sum > max_sum
        is_shorter = current_sum == max_sum and start == best_start and (i + 1 - start) < (best_end - best_start)

        if is_better or (current_sum == max_sum and start < best_start) or is_shorter:
            max_sum = current_sum
            best_start = start
            best_end = i + 1

    return numbers[best_start:best_end], max_sum

# проверка
print(max_sum_segment([-2, 3, -1, 4, -5, 2])) # ([3, -1, 4], 6)
print(max_sum_segment([-8, -3, -6])) # ([-3], -3))