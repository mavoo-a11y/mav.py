fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
cereals = ["rice","kamande", "wheat"]

groceries = [fruits,vegetables,cereals]

print(groceries[0])
for collection in groceries:
    for food in collection:
        print (food,end=" ")
        print()