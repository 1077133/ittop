# 1
# iq = int(input("Введи количество баллов: "))
#
# if 0 <= iq <= 60:
#     print("Плохо")
# elif 60 < iq <= 75:
#     print("Удовлетворительно")
# elif 75 < iq <= 90:
#     print("Хорошо")
# elif 90 < iq <= 100:
#     print("Отлично")
# else:
#     print("Некорректно")

# 2
# ax = float(input("Ax: "))
# ay = float(input("Ay: "))
# bx = float(input("Bx: "))
# by = float(input("By: "))
# cx = float(input("Cx: "))
# cy = float(input("Cy: "))
#
# if (bx - ax) * (cy - ay) - (by - ay) * (cx - ax) == 0:
#     print("Вырожденный")
#
# else:
#     ab2 = (bx - ax)**2 + (by - ay)**2
#     bc2 = (cx - bx)**2 + (cy - by)**2
#     ac2 = (cx - ax)**2 + (cy - ay)**2
#
#     if ab2 >= bc2 and ab2 >= ac2:
#         m = ab2
#         s = bc2 + ac2
#     elif bc2 >= ab2 and bc2 >= ac2:
#         m = bc2
#         s = ab2 + ac2
#     else:
#         m = ac2
#         s = ab2 + bc2
#
#     if s == m:
#         print("Прямоугольный")
#     elif s < m:
#         print("Тупоугольный")
#     else:
#         print("Остроугольный").

# 3
import random
n = random.randint(0,1000)

while 1:
    guess = int(input("Введи число: "))
    if guess < n:
        print(f"{guess} - меньше")
    elif guess > n:
        print(f"{guess} - больше")
    else:
        print(f"{guess} - угадал")
        break