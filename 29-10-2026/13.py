a = list(map(int, input().split()))
i = int(input())
if -len(a) <= i < len(a):
    print(a[i])
else:
    print('Нет такого индекса')
