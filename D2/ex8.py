base_price = 10
topping_price = 2.50
total_cost = base_price
tops = []


while True:
    topping = input("Enter a topping (or 'quit'): ").lower()      
    if topping == "quit":
        break
    else:
        tops.append(topping)
        print(f"Adding {topping} to your pizza!")
        total_cost += topping_price


if not tops:
    print("no Topping Added")
else:
    for top in tops:
        print(f"-{top}")

print(f"\nTotal Cost : {total_cost}")

