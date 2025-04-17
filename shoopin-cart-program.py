print("Marvin Shooping list")
food = []
prices = []
total = 0

while True:
    foods =input("Enter the food to buy(done to finish): ")
    if foods =="done":
        break
    else:
        price = float(input(f"Enter the price of a {foods}: $"))

food.append(foods)
prices.append(price)
print("----MY LIST ----")

for food in foods:
            print(food, end=" ")
            
for price in prices:
      total += price

print ()
print(f"Your total is: ${total}")