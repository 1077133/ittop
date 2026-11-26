numbers = list(map(int, input().split()))

a = [x ** 2 for x in numbers if x > 0]
b = [x ** 2 for x in numbers if x ** 2 > 0]

print(a)
print(b)