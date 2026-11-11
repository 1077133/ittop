warehouse_1 = {"ручка": 10, "тетрадь": 5}
warehouse_2 = {"ручка": 7, "карандаш": 12}
total = warehouse_1.copy()
for name, quantity in warehouse_2.items():
    if name in total:
        total[name] += quantity
    else:
        total[name] = quantity
print(total)
print("Всего:", sum(total.values()))
