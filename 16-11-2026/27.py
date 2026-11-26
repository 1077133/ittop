numbers = list(map(int, input().split()))

a = list(map(abs, filter(lambda x: abs(x) > 5, numbers)))
b = [abs(x) for x in numbers if abs(x) > 5]

print(a)
print(b)
