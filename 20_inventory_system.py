idx = 0
items = []

def add_item():
    """ create a new dictionary for a new item"""
    item_dict = {}
    name = input("Enter the name of the item: ")
    item_dict['Name'] = name
    price = input("Enter the price of the item: ")
    item_dict['Price'] = price
    quantity = input("Enter the quantity of the item: ")
    item_dict['Quantity'] = quantity
    category = input("Enter the category of the item: ")
    item_dict['Category'] = category
    return item_dict

def view_inventory(idx, item):
    """ Display all items """
    print("\nAll items created:")
    for idx, item in enumerate(items):
        print(f"\nItem {idx + 1}:")
        for key, value in item.items():
            print(f"{key}: {value}")

while True: # add an item
    item = add_item()
    items.append(item)
    another = input("Do you want to add another item? (yes/no): ").strip().lower()
    if another != 'yes':
        break

# view inventory
user = input("Do you want to view inventory? (yes/no): ").strip().lower()
if user == 'yes':
    view_inventory(idx, item)
