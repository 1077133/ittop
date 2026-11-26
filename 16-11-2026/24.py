rest = list(map(int, input().split()))
sold = list(map(int, input().split()))
a = list(map(lambda x, y: x - y, rest, sold))
print(a)
