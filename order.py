import random
import time

class Order:
    def __init__(self, order_id="", order_car=None, order_retailer=None, order_creation_time=None):
        self.order_id = order_id if order_id else self.generate_order_id(order_car.car_code)
        self.order_car = order_car
        self.order_retailer = order_retailer
        self.order_creation_time = order_creation_time if order_creation_time else int(time.time())

    def __str__(self):
        return f"{self.order_id}, {self.order_car.car_code}, {self.order_retailer.retailer_id}, {self.order_creation_time}"

    def generate_order_id(self, car_code):
        random_string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))
        modified_string = ''.join(random_string[i].upper() if i % 2 != 0 else random_string[i] for i in range(len(random_string)))
        ascii_codes = [str(ord(char)) for char in modified_string]
        remainder_indices = [str(int(code) ** 2 % len(ascii_codes)) for code in ascii_codes]
        final_string = ''.join(modified_string[i] * int(index) for i, index in enumerate(remainder_indices))
        return f"{final_string}{car_code}{int(time.time())}"


# Example usage:
order_creation_time = 1672491601
car_code = "MB123456"
order_id = Order.generate_order_id(car_code, order_creation_time)
print("Generated Order ID:", order_id)
