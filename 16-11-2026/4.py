numbers = list(map(int, input().split()))
a = [i ** 3 for i in numbers if i < 0]
print(a)
