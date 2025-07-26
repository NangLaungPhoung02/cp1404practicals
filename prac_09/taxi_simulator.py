"""CP1404
taxi_simulator.py
estimate time: 1 hour
actual time : 1: 30 minutes.
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Simulate driving different taxis and calculating fares. """
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 200, 4),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0.0

    print("Let's a drive!")
    display_menu()
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice =="d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                fare = drive_taxi(current_taxi)
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                total_bill += fare
        else:
            print("Invalid choice")
        print(f"Bill to date: ${total_bill:.2f}")
        display_menu()
        choice = input(">>>").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")



def display_menu():
    """Display menu option to the user."""
    print("Menu:\n C-Choose taxi\n D-Drive\n Q-Quit")

def choose_taxi(taxis):
    """Display taxis and allow user to select one. """
    print("Taxi available:")
    for i , taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Choose a taxi:"))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice.")
    except ValueError:
        print("Invalid input; please enter a number.")
    return None

def drive_taxi(taxi):
    """Drive the selected taxi a user-specified distance and return fare."""
    try:
        distance = float(input("Enter a distance:"))
        taxi.start_fare()
        taxi.drive(distance)
        return taxi.get_fare()
    except ValueError:
        print("Invalid input: please enter a number.")
        return 0.0

if __name__ == "__main__":
    main()
