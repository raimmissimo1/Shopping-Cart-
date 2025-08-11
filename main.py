print("========== Shopping Cart ==========")

total = 0
foods = []

while True:
    food = input("Enter food name (q to quit): ")
    if food.lower() == "q":
        break

    price = int(input("Enter price in tenge: "))
    foods.append((food, price))
    total += price

print("\n===== Your Cart =====")
for item, price in foods:
    print(f"{item} - {price}₸")

print(f"Total: {total}₸")
