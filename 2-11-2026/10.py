order = {
    "number": "A-102",
    "customer": {"name": "Максим", "email": "max@example.com"},
    "items": [
        {"title": "Тетрадь", "price": 80, "quantity": 3},
        {"title": "Ручка", "price": 50, "quantity": 2}
    ],
    "delivery": {"method": "курьер", "price": 200},
    "paid": False,
    "comment": None
}
for quantity in [3, 12]:
    order["items"][0]["quantity"] = quantity
    print("Заказ:", order["number"])
    print("Покупатель:", order["customer"]["name"])
    total = 0
    for item in order["items"]:
        cost = item["price"] * item["quantity"]
        print(item["title"], item["quantity"], cost)
        total += cost
    if total >= 1000:
        order["delivery"]["price"] = 0
    order["total"] = total + order["delivery"]["price"]
    print("Стоимость товаров:", total)
    print("Доставка:", order["delivery"]["price"])
    print("Итого:", order["total"])
    if order["paid"]:
        print("Заказ оплачен")
    else:
        print("Ожидает оплаты")
    if order["comment"] is None:
        print("Комментария нет")
    print()
