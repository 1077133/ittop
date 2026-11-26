names = input().split(",")
a = [name.strip() for name in names if name.strip() != ""]
print(a)
