people = input().split(",")
a = list(filter(lambda x: int(x.split()[1]) >= 60, people))
print(a)
