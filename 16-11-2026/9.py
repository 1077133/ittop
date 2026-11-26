rows = input().split(";")
a = [int(number) for row in rows for number in row.split() if int(number) > 0]
print(a)
