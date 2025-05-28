"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
SALE_THRESHOLD = 1000
LOW_DISCOUNT_RATE = 0.1
HIGH_DISCOUNT_RATE = 0.15
sale = float(input("Enter sales: $"))
while sale >= 0:
    if sale < SALE_THRESHOLD:
        discount_rate = LOW_DISCOUNT_RATE
    else:
        discount_rate =HIGH_DISCOUNT_RATE
    print ("Bonus= $", sale *discount_rate, sep="")
    sale = float(input("Enter sales: $"))
print ("No bonus is enough.")
