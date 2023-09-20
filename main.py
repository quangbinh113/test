import os
import random
import math
from car import Car
from car_retailer import CarRetailer
from order import Order

def main_menu():
    print("Car Purchase Advisor System")
    print("1. Look for the nearest car retailer")
    print("2. Get car purchase advice")
    print("3. Place a car order")
    print("4. Exit")

def generate_test_data():
    # Generate test data for cars and retailers
    cars = []
    retailers = []

    # Create 12 cars
    for _ in range(12):
        car_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + ''.join(random.choices('0123456789', k=6))
        car_name = f"Car {car_code}"
        car_capacity = random.randint(2, 7)
        car_horsepower = random.uniform(50, 300)
        car_weight = random.uniform(1000, 2500)
        car_type = random.choice(["FWD", "RWD", "AWD"])
        cars.append(Car(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type))

    # Create 3 car retailers with 4 cars in stock each
    for i in range(3):
        retailer_id = i + 1
        retailer_name = f"Retailer {retailer_id}"
        retailer_address = f"Address {retailer_id}, VIC {random.randint(3000, 3999)}"
        retailer_business_hours = (random.uniform(6, 10), random.uniform(16, 23))
        car_codes = [car.car_code for car in random.sample(cars, 4)]
        retailers.append(CarRetailer(retailer_id, retailer_name, retailer_address, retailer_business_hours, car_codes))

    return cars, retailers

def get_nearest_retailer(postcode, retailers):
    min_distance = math.inf
    nearest_retailer = None

    for retailer in retailers:
        retailer_postcode = int(retailer.carretailer_address.split()[-1])
        distance = abs(postcode - retailer_postcode)
        if distance < min_distance:
            min_distance = distance
            nearest_retailer = retailer

    return nearest_retailer

def get_car_purchase_advice(retailers):
    print("Available Car Retailers:")
    for retailer in retailers:
        print(f"{retailer.retailer_id}. {retailer.retailer_name}")

    retailer_choice = int(input("Select a retailer by entering its ID: "))
    selected_retailer = next((r for r in retailers if r.retailer_id == retailer_choice), None)

    if selected_retailer:
        print(f"Selected Retailer: {selected_retailer.retailer_name}")
        while True:
            print("Car Purchase Advice Menu:")
            print("1. Recommend a car")
            print("2. Get all cars in stock")
            print("3. Get cars in stock by car types")
            print("4. Get probationary licence permitted cars in stock")
            print("5. Back to Main Menu")

            advice_choice = input("Enter your choice (1/2/3/4/5): ")

            if advice_choice == '1':
                recommended_car = selected_retailer.car_recommendation()
                print(f"Recommended Car: {recommended_car.car_name}")
            elif advice_choice == '2':
                print("Cars in Stock:")
                for car in selected_retailer.carretailer_stock:
                    print(car)
            elif advice_choice == '3':
                car_types = input("Enter car types separated by commas (e.g., AWD,RWD): ").split(',')
                cars_by_type = selected_retailer.get_stock_by_car_type(car_types)
                if cars_by_type:
                    print("Cars by Car Types:")
                    for car in cars_by_type:
                        print(car)
                else:
                    print("No cars found for the specified car types.")
            elif advice_choice == '4':
                licence_type = input("Enter your licence type (L/P/Full): ").strip().upper()
                cars_for_licence = selected_retailer.get_stock_by_licence_type(licence_type)
                if cars_for_licence:
                    print("Cars permitted for your licence type:")
                    for car in cars_for_licence:
                        print(car)
                else:
                    print("No cars available for your licence type.")
            elif advice_choice == '5':
                break
            else:
                print("Invalid choice. Please select a valid option (1/2/3/4/5).")
    else:
        print("Invalid retailer ID. Please select a valid retailer.")

def place_car_order(retailers):
    print("Available Car Retailers:")
    for retailer in retailers:
        print(f"{retailer.retailer_id}. {retailer.retailer_name}")

    retailer_choice = int(input("Select a retailer by entering its ID: "))
    selected_retailer = next((r for r in retailers if r.retailer_id == retailer_choice), None)

    if selected_retailer:
        current_hour = float(input("Enter the current hour in 24H format (e.g., 12.5 for 12:30 PM): "))
        if selected_retailer.is_operating(current_hour):
            car_code = input("Enter the car code you want to order: ").strip().upper()
            if car_code in selected_retailer.carretailer_stock:
                order_id = generate_order_id(car_code, current_hour)
                order = Order(order_id, selected_retailer.get_car_by_code(car_code), selected_retailer, int(current_hour))
                selected_retailer.remove_from_stock(car_code)
                order.save_to_file("data/order.txt")
                print("Order placed successfully!")
                print(order)
            else:
                print("Car not available in the selected retailer's stock.")
        else:
            print("The selected retailer is currently closed.")
    else:
        print("Invalid retailer ID. Please select a valid retailer.")

def generate_order_id(car_code, order_creation_time):
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
    modified_string = ''.join([c.upper() if i % 2 == 1 else c for i, c in enumerate(random_string)])
    ascii_values = [ord(c) for c in modified_string]
    remainder_values = [val ** 2 % len(modified_string) for val in ascii_values]
    order_id = ''.join([modified_string[i] * remainder_values[i] for i in range(len(modified_string))])
    return f"{order_id}{car_code}{order_creation_time}"

def main():
    cars, retailers = generate_test_data()

    while True:
        main_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Functionality 3: Look for the nearest car retailer
            postcode = int(input("Enter your postcode: "))
            nearest_retailer = get_nearest_retailer(postcode, retailers)
            if nearest_retailer:
                print(f"The nearest car retailer is: {nearest_retailer.retailer_name}")
            else:
                print("No car retailers found.")
        elif choice == '2':
            # Functionality 4: Get car purchase advice
            get_car_purchase_advice(retailers)
        elif choice == '3':
            # Functionality 5: Place a car order
            place_car_order(retailers)
        elif choice == '4':
            print("Exiting the Car Purchase Advisor System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
