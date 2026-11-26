sizes = input().split(",")
a = list(map(lambda x: int(x.split()[0]) * int(x.split()[1]), sizes))
print(a)
