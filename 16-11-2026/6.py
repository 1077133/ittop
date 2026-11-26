numbers = list(map(int, input().split()))
a = ["чётное" if i % 2 == 0 else "нечётное" for i in numbers]
print(a)
