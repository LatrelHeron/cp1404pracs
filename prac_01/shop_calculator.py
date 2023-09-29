total_price = 0
item_total = int(input("Number of items: "))
for i in range(item_total):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price = total_price * 0.1
print(f"Total price for {item_total} items is ${total_price}")

