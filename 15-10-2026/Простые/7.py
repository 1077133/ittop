a = list(map(int, input().split()))
x = int(input())
k = 0
for n in a:
    if n == x:
        k += 1
print(k)
