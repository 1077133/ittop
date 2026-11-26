words = input().split(",")

a = list(filter(lambda x: x.startswith("го"), map(lambda x: x.strip().lower(), words)))
b = [x.strip().lower() for x in words if x.strip().lower().startswith("го")]

print(a)
print(b)
