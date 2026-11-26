people = input().split(",")

a = list(map(lambda x: x.split()[0], filter(lambda x: int(x.split()[1]) >= 18, people)))
b = [x.split()[0] for x in people if int(x.split()[1]) >= 18]

print(a)
print(b)
