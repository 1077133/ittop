a = list(map(int, input().split()))
n = len(a)
if n == 0:
    print('Центра нет')
elif n % 2 == 1:
    print(a[n // 2])
else:
    print(a[n // 2 - 1], a[n // 2])
