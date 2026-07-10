from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200,2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    print(taxi)
    print(f"Fare: ${fare:.2f}")
    assert round (fare, 2)== 48.80, f"Excepted $ 48.80, got ${fare:.2f}"

main()

