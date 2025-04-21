import unittest
from shelter import Tent, Tarp, Hammock


class TestShelter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.tent = Tent(4, "polyester", 6, 36, True, 12.5, True, 3)
        self.tent1 = Tent(2, "nylon", 7, 25, False, 13, False, 2)
        self.hammock = Hammock(2, "nylon", 3, 10)
        self.hammock1 = Hammock(1, "nylon", 4, 11, 10, 3)
        self.tarp = Tarp(5, "canvas", 4, 100, 5)
        self.tarp1 = Tarp(3, "nylon", 2, 80, 4, 3)

    def tearDown(self):
        del self.tent
        del self.tent1
        del self.hammock
        del self.tarp

    def test_str(self):
        print("Executing test_str")
        self.assertEqual(str(self.tent),
                         "Tent(4, polyester, 6, 36, True, 12.5, True, 3)")
        self.assertEqual(str(self.hammock),
                         "Hammock(2, nylon, 3, 10, 11, 3)")
        self.assertEqual(str(self.tarp),
                         "Tarp(5, canvas, 4, 100, 5, 3)")

    def test_lt(self):
        print("Executing test_lt")
        self.assertTrue(self.tent1 < self.tent)

        self.assertTrue(self.hammock1 > self.hammock)

        self.assertTrue(self.tarp1 < self.tarp)

    def test_is_better(self):
        print("Executing test_is_better")
        self.assertTrue(self.tent.is_better(self.tent1))

        self.assertTrue(self.hammock.is_better(self.hammock1))

        self.assertFalse(self.tarp.is_better(self.tarp1))


if __name__ == "__main__":
    unittest.main()