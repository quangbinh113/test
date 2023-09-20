class Car(object):
    """
    Class for car objects.
    """
    def __init__(self, car_code="XX000000", car_name="", car_capacity=0, car_horsepower=0, car_weight=0, car_type="FWD") -> None:
        self.car_code = car_code
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = car_type

    def __str__(self) -> str:
        return f"{self.car_code}, {self.car_name}, {self.car_capacity}, {self.car_horsepower}, {self.car_weight}, {self.car_type}"

    def probationary_licence_prohibited_vehicle(self) -> bool:
        # Calculate Power to Mass ratio in kilowatt per tonne
        power_to_mass_ratio = (self.car_horsepower / self.car_weight) * 1000
        # Check if it's a prohibited vehicle for probationary license drivers
        return power_to_mass_ratio > 130

    def found_matching_car(self, car_code_to_search: str) -> bool:
        return self.car_code == car_code_to_search

    def get_car_type(self) -> str:
        return self.car_type
