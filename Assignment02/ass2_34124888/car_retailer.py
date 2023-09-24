"""
Name: Quoc Khoa Tran
Date: 24/09/2023
Description: Create CarRetailer Class
"""

# Import libraries and modules
from retailer import Retailer  # Assuming Retailer class is defined in 'retailer.py'
from car import Car  # Assuming Car class is defined in 'car.py'
from order import Order
import random

path = r'E:\assignment\test\Assignment02\data\stock.txt'


class CarRetailer(Retailer):
    """
        Contains all the operations related to the CarRetailer Class. This class inherits from the Retailer class.
        Attributes
        ----------
        retailer_id : int
            must be unique integer of 8 digits
        retailer_name : str
            can only consist of letters and whitespace
        carretailer_address: str
            the address format will be street address followed by the state and postcode
        carretailer_business_hours : tuple
            a tuple of floats
            representing start and end hours in 24hr, e.g., (8.5,
            17.5) - business hours are from 8:30AM inclusive to
            5:30PM inclusive), the business hours should be
            within the range of 6:00AM inclusive to 11:00PM
            inclusive
        carretailer_stock : list
            a list of car_codes indicating the
            available cars from the retailer; the default value
            should be an empty list
        """
    def __init__(self, retailer_id: int, retailer_name: str, carretailer_address="",
                 carretailer_business_hours=(), carretailer_stock=[]) -> None:
        super().__init__(retailer_id, retailer_name)  # Inherit from Retailer class
        self.carretailer_address = carretailer_address
        self.carretailer_business_hours = carretailer_business_hours
        self.carretailer_stock = carretailer_stock
        self.car_list = []

    def __str__(self):  # Return the car retailer information as a formatted string.
        return f"{super().__str__()}, {self.carretailer_address}, {self.carretailer_business_hours}, {self.carretailer_stock}"

    def format_file(self, path: str) -> dict:
        # Convert the 'stock.txt' file to dictionary with key as retailer info, values as info of car stocks
        try:
            with open(path, 'r') as f:  # Open and read file
                lines = f.readlines()
                dic = {}
                for line in lines:
                    detail = line.strip().split(', ')
                    key = ', '.join(detail[:6])
                    dic[key] = []
                    lst = detail[6:]
                    for i in range(0, len(lst), 6):
                        car_info = lst[i:i + 6]
                        res = []
                        for val in car_info:
                            res.append(val.replace('[', '').replace(']', '').replace("'", ''))
                        dic[key].append(res)
            return dic
        except FileNotFoundError:
            print(f"Error: File '{path}' not found.")

    def update_stock_file(path: str, file_formatted: dict) -> None:
        # Open a file for writing
        with open(path, 'w') as file:
            # Iterate over the dictionary and write each entry to the file
            for key, value in file_formatted.items():
                for entry in value:
                    entry[0] = f"'{entry[0]}"
                # Convert the inner lists to a formatted string
                formatted_entries = [', '.join(entry) for entry in value]
                # Join the formatted entries into a single string
                formatted_data = "', ".join(formatted_entries)
                # Write the formatted data to the file
                file.write(f"{key}, [{formatted_data}']\n")

    def load_current_stock(self, path):
        """
        Load the current stock of the car retailer according to the retailer_id from
        the stock.txt file and store the car_codes of the Cars in a list; this list should
        be saved to carretailer_stock.
        Parameters
        ----------
        path: the path to open 'stock.txt' file

        Returns
        -------

        """
        stock = self.format_file(path)  # Call method format_file to get the dictionary of retailer and car stock
        for key, value in stock.items():
            if self.retailer_id in key:  # Check if retailer_id is in 'stock.txt' file
                for car in value:
                    self.carretailer_stock.append(car[0])  # Add the car_code to carretailer_stock list

    def is_operating(self, cur_hour):  # Check whether the car retailer is currently operating
        return self.carretailer_business_hours[0] <= cur_hour <= self.carretailer_business_hours[1]

    def get_all_stock(self):  # Check the information of all available cars currently in stock at the car retailer
        stock = self.format_file(path)  # Call method format_file to get the dictionary of retailer and car stock
        for key, value in stock.items():
            if str(self.retailer_id) in key:  # Check if retailer_id is in 'stock.txt' file
                for carinfo in value:
                    self.car_list.append(Car(carinfo[0], carinfo[1], carinfo[2], carinfo[3], carinfo[4], carinfo[5]))
                    # Append Car object to the car_list
        return self.car_list

    def get_postcode(self, path):  # Method to extract retailer postcode and stored as values in a dictionary
        with open(path, 'r') as f:  # Open and read 'stock.txt' file
            lines = f.readlines()
            dic = {}
            for line in lines:
                detail = line.strip().split(', ')
                key = int(detail[0])  # Append retailer_id to dictionary key
                dic[key] = detail[3]  # Assign retailer postcode as value of the key
        return dic

    def get_postcode_distance(self, postcode):
        # Return the absolute difference of the postcode input by the user and that of the car retailer
        postcode_dic = self.get_postcode(path)
        for key, value in postcode_dic.items():
            if key == self.retailer_id:  # Check if retailer_id is in 'stock.txt' file
                postcodenum_retailer = int(value[3:7])  # Extract the postcode number from the address
                distance = abs(postcode - postcodenum_retailer)  # Compute the absolute difference
                return distance

    def remove_from_stock(self, car_code):
        # Remove a car from the current stock at the car retailer. The car stock
        # should be consistent with the stock.txt file
        formattedfile = self.format_file(path)
        # Call method format_file to get the dictionary of retailer and car stock
        for key, value in formattedfile.items():
            for i, car_info in enumerate(value):
                if car_code in car_info:  # Check if car_code is in car stock
                    value.remove(car_info)  # Remove car_code from car stock
                    self.update_stock_file(path, formattedfile)  # Update in 'stock.txt' file
                    return True
        return False

    def add_to_stock(self, car):
        formattedfile = self.format_file(path)
        # Call method format_file to get the dictionary of retailer and car stock
        car_info = ", ".join(str(val) for val in [car.car_code, car.car_name, car.car_capacity,
                 car.car_horsepower, car.car_weight, car.car_type])
        # Create a list to store info of the car with each info as an item
        stock = self.get_all_stock()
        if car not in stock:  # Check whether the car is not in the retailer stock
            for retailer in formattedfile.keys():
                if str(self.retailer_id) in retailer:
                    formattedfile[retailer].append(car_info)  # Add the car info into the dictionary
                    self.update_stock_file(path, formattedfile)  # Update in the 'stock.txt' file
                    return True
        return False

    def get_stock_by_car_type(self, car_type):
        # Return the list of cars in the current stock by specific car_type values.
        list_by_car_type = []  # Create an empty list to store Car object
        stock = self.get_all_stock()
        for car in stock:
            if car_type == car.car_type:  # Check if car_type is in car stock
                list_by_car_type.append(car)  # Add the car to the list
        return list_by_car_type  # Return the list of result

    def get_stock_by_licence_type(self, license_type):
        # Return the list of cars in the current stock by specific car_type values.
        result = []  # Create a default empty list to store the result
        for car in self.car_list:  # Check if car is in stock
            if license_type == 'P':  # Check if the license type is probational
                if car.probationary_licence_prohibited_vehicle() is False:  # Check if the car is not prohibitted
                    result.append(car)  # Add the not prohibitted car to the list
            result.append(car) # Add cars of other license types to the list
        return result

    def car_recommendation(self):
        # Return a car that is randomly selected from the cars in stock at the current car retailer
        return random.choice(self.get_all_stock())

    def create_order(self, car_code):
        # Return an order object of a created order. When an order is created, the
        # car needs to be removed from the current stock of the car retailer. Such
        # updates need to be reflected in “stock.txt”. The created order needs to be
        # appended to “order.txt”.
        if car_code in self.carretailer_stock:  # Check if car_code is in car stock
            order = Order()  # Create an Order object named as order
            order.order_id = order.generate_order_id(car_code)  # Create a random order_id for order
            lst = self.get_all_stock()
            for car in lst:
                if car_code == car.car_code:  # Check if car is in car stock
                    order.order_car = car  # Add car to the value of order.order_car
            order.order_retailer = Retailer(self.retailer_id, self.retailer_name)
            string_order = order.__str__()  # Print order info as string
            with open(path, 'a') as f:  # Open and write 'order.txt' file
                f.write(f'\n{string_order}')  # Write to the end of the file


if __name__ == '__main__':
    stock = CarRetailer(12345678, 'Car Retailer', '123, Melbourne, VIC, 3000', (8.5, 17.5))
    car_list = stock.get_all_stock()
    print(stock.__str__())