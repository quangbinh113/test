import random

class Retailer:
    def __init__(self, retailer_id: int, retailer_name: str) -> None:
        # Initialize retailer attributes with default values
        self.retailer_id = retailer_id
        self.retailer_name = retailer_name

    def __str__(self) -> str:
        # Return retailer information as a formatted string
        return f"{self.retailer_id}, {self.retailer_name}"

    def generate_retailer_id(self, list_retailer):
        # Generate a unique retailer ID that is not in the list of existing retailer IDs
        while True:
            new_retailer_id = random.randint(10000000, 99999999)
            if new_retailer_id not in [retailer.retailer_id for retailer in list_retailer]:
                self.retailer_id = new_retailer_id
                break
