a = list(map(int, input().split()))
x = int(input())
k = -1
for i in range(len(a)):
    if a[i] == x:
        k = i
        break
print(k)
