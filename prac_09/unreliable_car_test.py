from prac_09.unreliable_car import UnreliableCar

def main():
    good_car = UnreliableCar("Thor", 100, 80)
    bad_car = UnreliableCar("Bob", 100, 10)
    for i in range(1, 12):
        print(f"Attempted to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")
    print(good_car)
    print(bad_car)

main()