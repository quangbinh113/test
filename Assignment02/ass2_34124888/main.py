"""
Name: Quoc Khoa Tran
Date: 24/09/2023
Description: Create Order Class
"""
# Import libraries and modules
import random
import string
from car import Car
from order import Order
from retailer import Retailer
from car_retailer import CarRetailer
import time


def main_menu():
    print("Car Purchase Advisor System")
    print("1. Look for the nearest car retailer")
    print("2. Get car purchase advice")
    print("3. Place a car order")
    print("4. Exit")


def generate_test_data():
    list_retailer = []
    # Create car retailers
    retailer1 = CarRetailer(None, "kfhjlskdhfgj", "City of Maroondah", "VIC3135", (8.8, 14.2))   
    retailer1.retailer_id = retailer1.generate_retailer_id(list_retailer)
    list_retailer.append(retailer1)
    retailer2 = CarRetailer(None, "dbjkassad", "Shire of Yarra Ranges", "VIC3160", (11.1, 13.4))
    retailer2.retailer_id = retailer2.generate_retailer_id(list_retailer)
    list_retailer.append(retailer2)
    retailer3 = CarRetailer(None, "fdgsdfdsgd", "City of Whittlesea", "VIC3754", (9.6, 16.5))
    retailer3.retailer_id = retailer3.generate_retailer_id(list_retailer)
    list_retailer.append(retailer3)

    # Generate and add cars to retailers' stock
    for i in range(4):
        r = Car()
        car_code = r.generate_car_code()
        car_name = ''.join(random.choice(string.ascii_letters) for i in range(6))
        car_capacity = random.randint(2, 5)
        car_horsepower = random.randint(100, 300)
        car_weight = random.randint(1000, 2000)
        car_type = random.choice(['FWD', 'RWD', 'AWD'])
        car = Car(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type)
        # Add cars to retailers' stock
        retailer1.add_to_stock(car)

    for i in range(4):
        r = Car()
        car_code = r.generate_car_code()
        car_name = ''.join(random.choice(string.ascii_letters) for i in range(6))
        car_capacity = random.randint(2, 5)
        car_horsepower = random.randint(100, 300)
        car_weight = random.randint(1000, 2000)
        car_type = random.choice(['FWD', 'RWD', 'AWD'])
        car = Car(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type)
        # Add cars to retailers' stock
        retailer2.add_to_stock(car)

    for i in range(4):
        r = Car()
        car_code = r.generate_car_code()
        car_name = ''.join(random.choice(string.ascii_letters) for i in range(6))
        car_capacity = random.randint(2, 5)
        car_horsepower = random.randint(100, 300)
        car_weight = random.randint(1000, 2000)
        car_type = random.choice(['FWD', 'RWD', 'AWD'])
        car = Car(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type)
        # Add cars to retailers' stock
        retailer3.add_to_stock(car)

    print(list_retailer)
    for car_retailer in list_retailer:
        car_retailer_info = car_retailer.__str__()
        retailer_stock = ', '.join([car.__str__() for car in car_retailer.get_all_stock()])
        with open(r'E:\assignment\test\Assignment02\data\stock.txt', 'a') as f:
            f.write(f"{car_retailer_info}, [{retailer_stock}]\n")



def find_nearest_retailer(postcode, list_retailer):
    dic = {}
    for o in list_retailer:
        car_retailer = CarRetailer(o.retailer_id, o.retailer_name)
        distance = car_retailer.get_postcode_distance(postcode)
        dic[car_retailer].append(distance)
    for key, value in dic.items():
        if value == min(dic.values()):
            return key


def get_car_purchase_advice(retailers):
    print("Available Car Retailers:")
    for retailer in retailers:
        print(f"{retailer.retailer_id}. {retailer.retailer_name}")
    selected_retailer = None
    # Prompt the user to select a car retailer
    selected_retailer_id = int(input("Select a car retailer by entering its ID: "))
    for retailer in CarRetailer.list_retailer:
        if selected_retailer_id == retailer.retailer_id:
            selected_retailer = retailer
            break

    if selected_retailer:
        while True:
            # Show sub-menu options
            print(f"\nSelected Retailer: {selected_retailer.retailer_name}\n")
            print("Options:")
            print("1. Recommend a car")
            print("2. Get all cars in stock")
            print("3. Get cars in stock by car types")
            print("4. Get probationary licence permitted cars in stock")
            print("5. Return to main menu")

            option = input("Enter your choice: ")
            if option == "1":
                # Recommend a random car
                recommended_car = selected_retailer.car_recommendation()
                print(f"Recommended Car: {recommended_car.car_name} ({recommended_car.car_code})")

            elif option == "2":
                # Get all cars in stock
                print(f"\nCars in Stock at {selected_retailer.retailer_name}:\n")
                for car in selected_retailer.car_list:
                    print(f"{car.car_name} ({car.car_code})")

            elif option == "3":
                # Get cars in stock by car types
                car_types = input("Enter car types (comma-separated, e.g., 'AWD,RWD'): ").split(',')
                print(f"\nCars in Stock at {selected_retailer.retailer_name} by Car Type:\n")
                for car_type in car_types:
                    car_type = car_type.strip()
                    matching_cars = selected_retailer.get_stock_by_car_type(car_type)
                    print(f"{car_type} Cars:")
                    for car in matching_cars:
                        print(f"{car.car_name} ({car.car_code})")

            elif option == "4":
                # Get probationary licence permitted cars in stock
                probationary_cars = selected_retailer.get_stock_by_licence_type('P')
                print(f"\nProbationary Licence Permitted Cars in Stock at {selected_retailer.retailer_name}:\n")
                for car in probationary_cars:
                    print(f"{car.car_name} ({car.car_code})")

            elif option == "5":
                break

        else:
            print("Invalid option. Please try again.")


def place_order():
    # Ask the user for retailer ID and car ID
    try:
        retailer_id, car_code = map(input("Enter retailer ID and car code (separated by space): ").split(''))
        retailer_id = int(retailer_id)
    except ValueError:
        print("Invalid input. Please enter codes separated by space.")
        return

    # Find the selected retailer
    selected_retailer = None
    for retailer in CarRetailer.list_retailer:
        if retailer_id == retailer.retailer_id:
            selected_retailer = retailer
            break

    if selected_retailer:
        # Check if the retailer is open during business hours
        current_hour = int(input("Enter the current hour (0-23): "))
        if selected_retailer.is_operating(current_hour):
            # Find the car to order
            car_to_order = None
            for car in selected_retailer.car_list:
                if car_code == car.car_code:
                    car_to_order = car
                    break

            if car_to_order:
                # Generate an order ID and create an Order object
                order_id = selected_retailer.generate_order_id(car_code)
                order = Order(order_id, car_to_order, selected_retailer, int(time.time()))

                # Append the order to "order.txt"
                with open('data/order.txt', 'a') as order_file:
                    order_file.write(str(order) + '\n')

                # Print order details to the user
                print(
                    f"Order placed successfully!\nOrder ID: {order_id}\nCar: {car_to_order.car_name} ({car_to_order.car_code})")
            else:
                print(f"Car with code {car_code} not found in stock.")
        else:
            print(f"The retailer is closed during the current hour ({current_hour}). Order cannot be placed.")
    else:
        print(f"Retailer with ID {retailer_id} not found.")


def place_car_order(retailers):
    print("Available Car Retailers:")
    for retailer in retailers:
        print(f"{retailer.retailer_id}. {retailer.retailer_name}")

    retailer_choice = int(input("Select a retailer by entering its ID: "))
    selected_retailer = None
    for retailer in CarRetailer.list_retailer:
        if retailer_choice == retailer.retailer_id:
            selected_retailer = retailer
            break

    if selected_retailer:
        current_hour = float(input("Enter the current hour in 24H format (e.g., 12.5 for 12:30 PM): "))
        if selected_retailer.is_operating(current_hour):
            car_code = input("Enter the car code you want to order: ").strip().upper()
            if car_code in selected_retailer.carretailer_stock:
                order_id = selected_retailer.generate_order_id(car_code, current_hour)
                order = Order(order_id, selected_retailer.get_car_by_code(car_code), selected_retailer,
                              int(current_hour))
                selected_retailer.create_order(car_code)
                print("Order placed successfully!")
                print(order)
            else:
                print("Car not available in the selected retailer's stock.")
        else:
            print("The selected retailer is currently closed.")
    else:
        print("Invalid retailer ID. Please select a valid retailer.")


def main():
    list_retailer = []
    generate_test_data()

    while True:
        main_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Functionality 3: Look for the nearest car retailer
            postcode = int(input("Enter your postcode: "))
            nearest_retailer = find_nearest_retailer(postcode, list_retailer)
            if nearest_retailer:
                print(f"The nearest car retailer is: {nearest_retailer.retailer_name}")
            else:
                print("No car retailers found.")
        elif choice == '2':
            # Functionality 4: Get car purchase advice
            get_car_purchase_advice(list_retailer)
        elif choice == '3':
            # Functionality 5: Place a car order
            place_car_order(list_retailer)
        elif choice == '4':
            print("Exiting the Car Purchase Advisor System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")


if __name__ == "__main__":
    generate_test_data()
