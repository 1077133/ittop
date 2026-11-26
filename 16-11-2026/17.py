orders = input().split(",")
a = list(filter(lambda x: int(x.split()[1]) == 1 and int(x.split()[0]) >= 300, orders))
print(a)
