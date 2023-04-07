import json

# 1
def shopping_list():
    with open('data.json', 'wb'):
        pass
    i = 0
    all_data = {0: 0}
    while True:
        purchase_name = input("Введите название продукта (стоп - для выхода) ")

        if purchase_name == "стоп":
            break
        else:
            try:
                purchase_price = float(input("Введите цену товара"))
                data = {"product name": purchase_name,
                        "cost": purchase_price}
                all_data[i] = data
                i += 1
            except Exception:
                print("Проверьте стоимость товара")

        with open("data.json", 'w') as file_json:
            json.dump(all_data, file_json, ensure_ascii=False)


shopping_list()

# 2

with open("data.json") as file:
    data = json.load(file)
    cost = 0
    print("ваш список продуктов:")
    for key, value in data.items():
        print(f"{value['product name']} - {value['cost']} руб.")
        cost += int(value["cost"])

print("============================")
print(f"итоговая сумма - {cost}")
