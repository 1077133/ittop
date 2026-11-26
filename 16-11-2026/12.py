numbers = list(map(int, input().split()))
a = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))
print(a)
