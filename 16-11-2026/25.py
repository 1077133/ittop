numbers = list(map(int, input().split()))

a = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
b = [x ** 2 for x in numbers if x % 2 != 0]

print(a)
print(b)
