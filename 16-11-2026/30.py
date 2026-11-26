numbers = list(map(int, input().split()))

f = filter(bool, numbers)
print(list(f))
print(list(f))

m = map(abs, numbers)
print(list(m))
print(list(m))
