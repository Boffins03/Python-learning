# Define food items and their prices
menu = {'Pizza': 70, 'Burger': 50, 'Momo': 30, 'Chips': 10}

print("Food Menu")
# Print the menu
for item, price in menu.items():
    print(f'{item}: {price}')

order = input("Enter your order (e.g., '2 Pizza, 1 Burger'): ")

# Split the order string into items and quantities
items = order.split(',')
order_dict = {}

# Parse each item and quantity
for item in items:
    item = item.strip()  # Remove leading/trailing spaces
    quantity, food_item = item.split(' ')
    quantity = int(quantity)
    food_item = food_item.capitalize()  # Capitalize the first letter for consistency

    if food_item in menu:
        if food_item in order_dict:
            order_dict[food_item] += quantity
        else:
            order_dict[food_item] = quantity
    else:
        print(f"Sorry, '{food_item}' is not available on the menu.")

# Calculate the total amount
total_amount = sum(menu[item] * quantity for item, quantity in order_dict.items())

# Print the order summary
print("\nYour Order:")
for item, quantity in order_dict.items():
    print(f"{item}: {quantity}")
print(f"Total Amount: {total_amount}")
