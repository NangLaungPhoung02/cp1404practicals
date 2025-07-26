"""Cp1404
unreliable_car_test.py
estimate time: 30 minutes
actual  total two file time: 45 minutes"""

from unreliable_car import UnreliableCar

def main():
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    unreliable_car = UnreliableCar("Sketchy", 100, 20)

    print("Testing mostly reliable car. ")
    for i in range(10):
        distance = reliable_car.drive(10)
        print(f"Attempt {i+1}:Drove {distance}km")

    print("\nTesting Sketchy car. ")
    for i in range(10):
        distance = unreliable_car.drive(10)
        print(f"Attempt {i+1}: Drove {distance}km")

if __name__=="__main__":
    main()
