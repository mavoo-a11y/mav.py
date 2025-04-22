menu = {"Pizza": 5.99, "Burger": 6.00, "Fries": 2.49, "Soda": 1.99}
cart = []
total = 0

print("-------------MENU-------------")

for key ,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------WELCOME & ENJOY------")

while True:
    food = input("Select an item from the menu( done to finish): ")
    if food=="done":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------YOUR ORDER FOR TODAY---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
print("Thank you for your order!")
print("Have a great day!")
print("Please come again!")
