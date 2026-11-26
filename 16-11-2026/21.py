seconds = list(map(int, input().split()))
a = list(map(lambda x: (x // 60, x % 60), seconds))
print(a)
