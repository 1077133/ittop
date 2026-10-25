a = list(map(int, input().split()))
answer = 'ДА'
for i in range(1, len(a)):
    if a[i] < a[i - 1]:
        answer = 'НЕТ'
        break
print(answer)
