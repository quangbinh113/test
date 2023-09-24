from retailer import Retailer  # Assuming Retailer class is defined in 'retailer.py'
from car import Car  # Assuming Car class is defined in 'car.py'
import random

PATH_STOCK = r'E:\assignment\test\data\stock.txt'

def get_car_code(PATH: str) -> dict:
    try:
        with open(PATH, 'r') as f:
            lines = f.readlines()
            dic = {}
            for line in lines:
                detail = line.strip().split(', ')
                key = int(detail[0])
                dic[key] = []
                lst = detail[6:]
                for i in range(0, len(lst), 6):
                    car_info = lst[i:i+6]
                    res = []
                    for val in car_info:
                        res.append(val.replace('[', '').replace(']', '').replace("'", ''))
                    dic[key].append(res)
        return dic
    except FileNotFoundError:
        print(f"Error: File '{PATH_STOCK}' not found.")


class CarRetailer(Retailer):
    def __init__(self, retailer_id: int, retailer_name: str, carretailer_address="", 
                 carretailer_business_hours=(), carretailer_stock=[]) -> None:
        
        super().__init__(retailer_id, retailer_name)  # Inherit from Retailer class
        self.carretailer_address = carretailer_address
        self.carretailer_business_hours = carretailer_business_hours
        self.carretailer_stock = []
        self.all_stock = [object, object, object]


    def __str__(self):
        return f"{super().__str__()}, {self.carretailer_address}, {self.carretailer_business_hours}, {self.carretailer_stock}"

    def load_current_stock(self, path):
        stock = get_car_code(path)
        for key, value in stock.items():
            if key == self.retailer_id:
                for car in value:
                    self.carretailer_stock.append(car[0])

    def is_operating(self, cur_hour):
        # Check if the car retailer is currently operating based on business hours
        start_hour, end_hour = self.carretailer_business_hours
        return start_hour <= cur_hour <= end_hour

    def get_all_stock(self):
        try:
            with open(PATH_STOCK, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    detail = line.strip().split(', ')
                    if int(detail[0]) == self.retailer_id:
                        available_cars = detail[-1]
                        for car_info in available_cars:
                            info = car_info.split(', ')
                            car = Car(info[0], info[1], info[2], info[3], info[4], info[5])
                            self.all_stock.append(car)
            return self.all_stock
        except FileNotFoundError:
            print(f"Error: File '{PATH_STOCK}' not found.")

    def get_postcode_distance(self, postcode):
        # Extract the postcode from carretailer_address and calculate the absolute difference
        retailer_postcode = int(self.carretailer_address.split()[-1])
        return abs(postcode - retailer_postcode)

    def remove_from_stock(self, car_code):
        for car_info in self.carretailer_stock:
            if car_code == car_info[0]:
                self.carretailer_stock.remove(car_info)
                self.update_stock_file()  # Update the stock file
                return True
        return False

    def update_stock_file(self):
        try:
            with open('data/stock.txt', 'r') as file:
                lines = file.readlines()

            # Update the stock data for this retailer in the lines
            for i, line in enumerate(lines):
                retailer_info = line.strip().split(', ')
                retailer_id = int(retailer_info[0])
                if retailer_id == self.retailer_id:
                    # Remove the car from this retailer's stock
                    for car_info in self.carretailer_stock:
                        car_code = car_info[0]
                        lines[i] = lines[i].replace(f"'{car_code}', ", '')  # Remove the car entry from the line

            # Write the updated lines back to the stock file
            with open('data/stock.txt', 'w') as file:
                file.writelines(lines)
        except FileNotFoundError:
            print(f"Error: File 'data/stock.txt' not found.")

    def add_to_stock(self, car):
        # Add a car to the current stock at the car retailer
        if car.car_code not in self.carretailer_stock:
            self.carretailer_stock.append(car.car_code)
            return True
        else:
            return False  # Car already exists in stock

    def get_stock_by_car_type(self, car_types):
        # Return a list of cars in the current stock by specific car_type values
        return [car for car in self.carretailer_stock if Car(car).get_car_type() in car_types]

    def get_stock_by_licence_type(self, licence_type):
        # Return a list of cars in the current stock that are not forbidden by the driver’s licence type
        return [car for car in self.carretailer_stock if not Car(car).probationary_licence_prohibited_vehicle()]

    def car_recommendation(self):
        # Return a random car from the cars in stock
        if self.carretailer_stock:
            return random.choice(self.carretailer_stock)

    # def create_order(self, car_code):
    #     # Create an order object, remove the car from stock, and update files
    #     if self.remove_from_stock(car_code):
    #         # Create an order object and append it to 'order.txt'
    #         order_id = self.generate_order_id(car_code)
    #         order_time =  # Get the current timestamp
    #         with open("data/order.txt", "a") as order_file:
    #             order_file.write(f"{order_id}, {car_code}, {self.retailer_id}, {order_time}\n")
    #         return True
    #     else:
    #         return False  # Car not found in stock

    # def generate_order_id(self, car_code):
    #     # Generate a unique order ID based on car_code and order creation time
    #     # You can implement this based on the provided steps in your assignment
    #     pass  # Implement this method based on assignment requirements

if __name__ == "__main__":

    r = CarRetailer(88727858, 'dLrIrEaovi')
    r.load_current_stock(PATH_STOCK)

    print(r.carretailer_stock)
    print(type(r))
    r.remove_from_stock('BY962504')

    