# test_autompg.py
import unittest
from autompg import AutoMPG, AutoMPGData
import os


class TestAutoMPG(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.auto_data = AutoMPGData()  # Create the AutoMPGData instance.

    @classmethod
    def tearDownClass(cls):
        # Delete the cleaned auto-mpg file.
        if os.path.exists("auto-mpg.clean.txt"):
            os.remove("auto-mpg.clean.txt")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_str(self):
        print("Executing test_str")
        test_car = self.auto_data.data[0]
        expected_format = f"AutoMPG('{test_car.make}','{test_car.model}',{test_car.year},{test_car.mpg})"
        self.assertEqual(str(test_car), expected_format)

    def test_eq(self):
        print("Executing test_eq")
        car1 = AutoMPG("Toyota", "Corolla", 2020, 30.5)
        car2 = AutoMPG("Toyota", "Corolla", 2020, 30.5)
        self.assertTrue(car1 == car2)

        car3 = AutoMPG("Ford", "Focus", 2020, 30.5)
        self.assertFalse(car1 == car3)

    def test_lt(self):
        print("Executing test_lt")
        car1 = AutoMPG("Toyota", "Camry", 2015, 25.5)
        car2 = AutoMPG("Toyota", "Corolla", 2020, 30.5)
        self.assertTrue(car1 < car2)

    def test_hash(self):
        print("Executing test_hash")
        car1 = AutoMPG("Toyota", "Corolla", 2020, 30.5)
        car2 = AutoMPG("Toyota", "Corolla", 2020, 30.5)
        self.assertEqual(hash(car1), hash(car2))


if __name__ == "__main__":
    unittest.main()
