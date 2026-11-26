
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

player = "X"
moves = 0

while True:
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

    print("Ход игрока", player)

    try:
        number = int(input("Выберите клетку (1-9): "))
    except ValueError:
        print("Введите число!")
        continue

    if number < 1 or number > 9:
        print("Нет такой клетки!")
        continue

    if board[number - 1] == "X" or board[number - 1] == "O":
        print("Клетка занята!")
        continue

    board[number - 1] = player
    moves += 1

    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):
        
        print("Победил игрок", player)
        break

    if moves == 9:
        print("Ничья!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

print()
print(board[0], "|", board[1], "|", board[2])
print("--+---+--")
print(board[3], "|", board[4], "|", board[5])
print("--+---+--")
print(board[6], "|", board[7], "|", board[8])
