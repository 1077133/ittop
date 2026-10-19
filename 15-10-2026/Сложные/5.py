def longest_increasing_run(numbers):
    if not numbers: return []

    max_run = [numbers[0]]
    current_run = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_run.append(numbers[i])
        else:
            if len(current_run) > len(max_run):
                max_run = current_run
            current_run = [numbers[i]]

    if len(current_run) > len(max_run):
        max_run = current_run

    return max_run

# проверка
print(longest_increasing_run([3, 5, 7, 2, 4, 6, 8, 1])) # [2, 4, 6, 8]
print(longest_increasing_run([1, 2, 2, 3, 4])) # [2, 3, 4]
print(longest_increasing_run([9, 7, 5])) # [9]
