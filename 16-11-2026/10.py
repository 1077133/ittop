numbers = list(map(int, input().split()))
a = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
print(a)
