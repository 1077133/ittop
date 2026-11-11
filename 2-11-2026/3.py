prices = {"хлеб": 50, "молоко": 90, "сыр": 150, "яблоко": 30}
name = input("Товар: ")
quantity = int(input("Количество: "))
if name in prices:
    print("Стоимость:", prices[name] * quantity)
else:
    print("Товар не найден")
print("Товары не дороже 100 рублей:")
for name, price in prices.items():
    if price <= 100:
        print(f"{name}: {price}")
