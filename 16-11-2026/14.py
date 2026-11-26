files = input().split()
a = list(filter(lambda x: x.lower().endswith(".py"), files))
print(a)
