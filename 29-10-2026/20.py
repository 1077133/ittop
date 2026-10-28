a = list(map(int, input().split()))
n = len(a)
for i in range(n // 2):
    j = n - 1 - i
    print(i, a[i], j, a[j])
if n % 2 == 1:
    print(n // 2, a[n // 2])
