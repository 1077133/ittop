words = input().split()
a = list(map(lambda x: (x[0], x[-1]), words))
print(a)
