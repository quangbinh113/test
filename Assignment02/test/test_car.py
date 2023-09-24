from unittest import TestCase

from ass2_34124888.car import Car


class TestCar(TestCase):

    def test_probationary_licence_prohibited_vehicle_return_false(self):
        car = Car("MB123456", "Mercedes-Benz", 5, 100, 2000, "FWD")

        actual = car.probationary_licence_prohibited_vehicle()

        expected = False
        self.assertEqual(expected, actual)

    def test_probationary_licence_prohibited_vehicle_return_true(self):
        car = Car("MB123456", "Mercedes-Benz", 5, 620, 3500, "FWD")

        actual = car.probationary_licence_prohibited_vehicle()

        expected = True
        self.assertEqual(expected, actual)

    def test_found_matching_car_True(self):
        car = Car("MB123456", "Mercedes-Benz", 5, 620, 3500, "FWD")
        actual = car.found_matching_car("MB123456")
        expected = True
        self.assertEqual(expected, actual)

    def test_found_matching_car_False(self):
        car = Car("MB123456", "Mercedes-Benz", 5, 620, 3500, "FWD")
        actual = car.found_matching_car("MB123457")
        expected = False
        self.assertEqual(expected, actual)