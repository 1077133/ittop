product = {
    "id": 42,
    "title": "Наушники",
    "price": 3500,
    "in_stock": True,
    "tags": ["техника", "звук"],
    "specs": {"wireless": True, "battery_hours": 30, "color": "чёрный"},
    "reviews": [
        {"author": "Иван", "rating": 5, "text": "Хороший звук"},
        {"author": "Ольга", "rating": 4, "text": "Удобные"}
    ]
}
print("Название:", product["title"])
print("Цена:", product["price"])
print("Цвет:", product["specs"]["color"])
print("Время работы:", product["specs"]["battery_hours"])
product["price"] *= 0.9
if "скидка" not in product["tags"]:
    product["tags"].append("скидка")
product["reviews"].append({"author": "Анна", "rating": 3, "text": "Быстро разряжаются"})
total = 0
print("Авторы отзывов с оценкой ниже 4:")
for review in product["reviews"]:
    total += review["rating"]
    if review["rating"] < 4:
        print(review["author"])
product["rating"] = total / len(product["reviews"])
print("Новая цена:", product["price"])
print("Средняя оценка:", product["rating"])
if product["in_stock"] and product["specs"]["wireless"]:
    print("Можно заказать")
else:
    print("Не подходит")
