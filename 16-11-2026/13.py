numbers = list(map(int, input().split()))
left, right = map(int, input().split())
a = list(filter(lambda x: left <= x <= right, numbers))
print(a)
