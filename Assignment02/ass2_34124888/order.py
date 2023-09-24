"""
Name: Quoc Khoa Tran
Date: 24/09/2023
Description: Create Order Class
"""

# Import libraries and modules
import random
import time
import string
from car import Car
from retailer import Retailer


class Order:
    """
        Contains all the operations related to an Order.
        Attributes
        ----------
        order_id : str
            must be unique strings
        order_car : object
            the car object related to this order
        order_retailer: object
            the retailer object related to this order
        car_horsepower : int
            a string to store the video Id to be played.
        order_creation_time : int
            the UNIX timestamp of the order creation
        """
    def __init__(self, order_id='', order_car=Car(), order_retailer=Retailer(), order_creation_time=0):
        self.order_id = order_id
        self.order_car = order_car
        self.order_retailer = order_retailer
        self.order_creation_time = order_creation_time if order_creation_time else int(time.time())

    def __str__(self):  # Return the user information as a formatted string
        return ','.join([str(self.order_id), str(self.order_car),
                         str(self.order_retailer), str(self.order_creation_time)])

    def generate_order_id(self, car_code):  # Return a unique order ID
        # Step 1: Generate a random string of 6 lowercase alphabetic characters
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
        # Step 2: Convert every second character to uppercase
        random_string = ''.join([char.upper() if i % 2 == 1 else char for i, char in enumerate(random_string)])
        # Step 3: Get ASCII codes for characters in Step 2
        ascii_codes = [ord(char) for char in random_string]
        # Step 4: Calculate powered ASCII codes and get remainders
        str_1 = "~!@#$%^&*"
        powered_remainders = [(code ** 2) % len(str_1) for code in ascii_codes]
        # Step 5: Use remainders as indexes to obtain corresponding characters from str_1
        transformed_chars = [str_1[remainder] for remainder in powered_remainders]
        # Step 6: Append characters from Step 5 n times
        final_order_id = ''
        for i, char in enumerate(random_string):
            n = i + 1  # n is the index of the character in the string from Step 2
            final_order_id += transformed_chars[i] * n
        final_order_id = random_string + final_order_id
        # Step 7: Append car_code and order creation time
        str_order_creation_time = self.order_creation_time
        final_order_id += car_code + str_order_creation_time  # Replace order_creation_time with the actual time
        return final_order_id
