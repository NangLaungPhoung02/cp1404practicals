total_price = 0
number_of_item = int(input("Enter the number of item:"))
while number_of_item <= 0:
    print ("Invalid input")
    number_of_item = int(input("Enter the number of item:"))
for i in range (1,number_of_item + 1):
    price_of_each_item = float(input("Enter the price of each item:"))
    while price_of_each_item <= 0:
        print("Invalid input")
        price_of_each_item = float(input("Enter the price of each item:"))
    total_price += price_of_each_item

if total_price > 100:
    total_price *= 0.9

print (f"total price for {number_of_item} is $ {total_price:.2f}")