"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    number_of_months = int(input("How many number_of_months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}:"))
        incomes.append(income)

    print("\nIncome Report\n-------------")

    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

def print_income():
    """ Display income report for incomes over a given number of month. """
    total_incomes=[]
    number_of_months = int(input("How many number_of_months"))
    for month,income in enumerate (total_incomes, start = 1):
        total_incomes += income
        print (f"Month {month:2} - income: $ {income :10.2f} total: ${total_incomes :10.2f}")


main()