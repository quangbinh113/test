"""
Name: Quoc Khoa Tran
Date: 24/09/2023
Description: Create Retailer Class
"""

# Import libraries and modules
import random

class Retailer:
    """
        Contains all the operations related to a retailer.
        Attributes
        ----------
        retailer_id : str
            must be unique integer of 8 digits
        retailer_name : str
        """
    list_retailer = []  # A default list to store all the existing Retailer

    def __init__(self, retailer_id=None, retailer_name=''):
        self.retailer_id = retailer_id
        self.retailer_name = retailer_name

    def __str__(self):
        return str(self.retailer_id) + ',' + str(self.retailer_name)

    def generate_retailer_id(self, list_retailer):
        """
        generate an unique retailer_id (use random to generate a 8 digits int number)

        Arguments
        ----------
            list_retailer: list
                A list of all existing retailers (default is empty list)

        Returns
        ----------
        new_retailer_id: int
            new randomly generated retailer id
        """
        list_retailer.append(Retailer)
        new_retailer_id = random.randint(10000000, 99999999)  # Create a random retailer_id of 8 digits
        existing_retailer_id = [item.retailer_id for item in Retailer.list_retailer]
        while True:  # keep checking until find the unique one
            if new_retailer_id in existing_retailer_id:
                new_retailer_id = random.randint(10000000, 99999999)  # Recreate a new retailer_id if existed
            else:
                break
        self.retailer_id = new_retailer_id  # Assign retailer_id with generated random id
