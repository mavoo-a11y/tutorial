shoes = {"Nike": 100, "Adidas": 80, "Puma": 60}
cart= []
total = 0

print("-----WELCOME-----")

for key , value in shoes.items():
    print(f"{key}: ${value}")
print("-----BEST PLACE TO SHOP-----")

while True:
    choice = input("Enter the name of the shoe you want to buy (done to finish): ")
    if choice== "done":
        break
    elif shoes.get(choice) is not None:
         cart.append(choice)
   
print("----- YOUR PURCHASE FOR TODAY-------")

for item in cart:
    print(f"{item}: ${shoes[item]}")
    total += shoes[item]

print(f"Total: ${total}")

print()
print("------THANK YOU FOR SHOPPING WITH US ------")


