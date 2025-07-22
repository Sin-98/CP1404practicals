from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive"

def main():
    """The main function of a taxi simulator program."""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != q:
        if menu_choice == "c":
            print("Taxis available: ")


