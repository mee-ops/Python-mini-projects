menu = {
    'Pizza': 100,
    'Burger': 80,
    'Pasta': 90,
    'Maggie': 65,
    'Coffee': 120,
    'Hot Chocolate':110,
    'Strawberry Icecream':150
}

print("welcome to cafe restaurant")
print("Pizza : Rs.100 \nBurger : Rs.80 \nPasta :  Rs.90 \nMaggie :  Rs.65 \nCoffee :  Rs.120 \nHot Chocolate :  Rs.110 \nStrawberry Icecream :  Rs.150")

order_Total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_Total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"ordered item{item_1} is not avaiable yet")

another_order = input("Do u want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second order = ")
    if item_2 in menu:
        order_Total += menu[item_2]
        print(f"Item {item_2} has been added to order ")
    else:
        print(f"Ordered item {item_2} is not avaiable!")
print(f"The total amount of items to pay is {order_Total}")            