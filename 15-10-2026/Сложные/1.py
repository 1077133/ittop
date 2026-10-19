def unique_orders(numbers):
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result

# проверка
print(unique_orders([4, 2, 4, 7, 2, 9, 7, 1])) # из условия - [4, 2, 7, 9, 1]
print(unique_orders([])) # пустой - []
print(unique_orders([5, 5, 5, 5, 5,])) # повторы - [5]
print(unique_orders([1, 1, 2, 2, 3, 3])) # еще чото - [1, 2, 3]