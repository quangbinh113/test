"""
Name: Quoc Khoa Tran
Date: 24/09/2023
Description: Create Car Class
"""
# Import libraries and modules
import random
import string


class Car:
    """
    Contains all the operations related to a car.
    Attributes
    ----------
    car_code : str
         must be unique and in the format of
        two uppercase letters plus 6 digits, e.g.,
        MB123456
    car_name : str
    car_capacity: int
        (Each car has a maximum seating
        capacity)
    car_horsepower : int
        a string to store the video Id to be played.
    car_weight: int
        the car_weight is the
        tare weight of the vehicle (the weight of an empty
        standard vehicle with all of its fluids and
        specifically 10 litres of fuel in the tank)
    car_type: int
        values should be one of “FWD”, “RWD”
        or “AWD”

    """
    car_code_list = []  # A list to store all existing car_code

    def __init__(self, car_code='XX000000', car_name='', car_capacity=0,
                 car_horsepower=0, car_weight=0, car_type='FWD'):
        self.car_code = self.car_code_validate(car_code)
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = self.car_type_validate(car_type)

    def __str__(self):
        return f"'{self.car_code}, {self.car_name}, {self.car_capacity}, {self.car_horsepower}, {self.car_weight}, {self.car_type}'"
        
    def car_code_validate(self, car_code):
        """
        To validate the car_code must be in correct format 2 upper letters and 6 digits

        Arguments
        ----------
        car_code : str
            The car_code to be validated (default is empty String)

        """
        if len(car_code) == 8 and car_code[:2].isupper() and car_code[2:].isdigit():
            return car_code
        else:
            print("Please input the correct car code in the format 'XX123456' (two uppercase letters plus 6 digits)")

    def generate_car_code(self):
        """
        To generate a random car_code in correct format 2 upper letters and 6 digits

        No Argument
        ----------

        """
        random_letters = ''.join(random.choices(string.ascii_uppercase, k=2))  # Generate 2 random upper letters
        random_digits = ''.join(random.choices(string.digits, k=6))  # Generate 6 random digits
        new_car_code = random_letters + random_digits  # Connect 2 letters and 6 digits to create car_code
        existing_car_code = [item.car_code for item in Car.car_code_list]  # Call list of existing car_code
        while True:
            if new_car_code in existing_car_code:
                new_car_code = random_letters + random_digits  # Create a new car_code if car_code existed
            else:
                break
        return new_car_code

    def car_type_validate(self, car_type):
        """     
        To generate a random car_code in correct format 2 upper letters and 6 digits

        Arguments
        ----------
        car_type : str
            The car_type to be validated (default is 'FWB')
        """
        correct_car_type = ['FWD', 'RWD', 'AWD']  # Create a list of correct car_types
        if car_type not in correct_car_type:  # Check if car_type is in the list of correct car_types
            print("Please input the correct car type (FWD, RWD, or AWD)")
        else:
            return car_type

    def __str__(self):
        """
                To generate a random car_code in correct format 2 upper letters and 6 digits

                No Argument
                ----------

        """
        return ','.join([str(self.car_code), str(self.car_name), str(self.car_capacity),
                         str(self.car_horsepower), str(self.car_weight), str(self.car_type)])

    def probationary_licence_prohibited_vehicle(self):
        """
                To check whether the vehicle is a prohibited vehicle for probationary licence drivers

                No Argument
                ----------
        """
        return round(self.car_horsepower / self.car_weight * 1000) > 130

    def found_matching_car(self, car_code):
        """
                To check whether the current vehicle is the one to be found based on a car_code

                Arguments
                ----------
                car_code : str
                    The car_code of the car to be searched (default is Empty String)
                """
        return car_code == self.car_code

    def get_car_type(self):
        """
                To return the car_type of the current car

                No Argument
                ----------
                """
        return str(self.car_type)


if __name__ == '__main__':
    car = Car()
    code =  car.generate_car_code()
    print(code)