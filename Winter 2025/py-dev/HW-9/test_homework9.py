# Imports
import unittest
from homework9 import Distributions, NumpyDistribution


class TestDistributions(unittest.TestCase):
    """
    Tests for the Distributions class (using Python's built-in random).
    """

    def test_normal_distribution_valid(self):
        """
        Test creating a valid normal distribution.
        """
        dist_obj = Distributions(dist="normal", mean=0, std=1, size=100)
        self.assertEqual(dist_obj.distribution, "normal")
        self.assertEqual(dist_obj.mean, 0)
        self.assertEqual(dist_obj.std, 1)
        self.assertEqual(dist_obj.size, 100)
        self.assertEqual(len(dist_obj.samples), 100)

    def test_lognormal_distribution_valid(self):
        """
        Test creating a valid lognormal distribution.
        """
        dist_obj = Distributions(dist="lognormal", mean=1, std=5, size=50)
        self.assertEqual(dist_obj.distribution, "lognormal")
        self.assertEqual(dist_obj.mean, 1)
        self.assertEqual(dist_obj.std, 5)
        self.assertEqual(dist_obj.size, 50)
        self.assertEqual(len(dist_obj.samples), 50)

    def test_laplace_distribution_valid(self):
        """
        Test creating a valid laplace distribution.
        """
        dist_obj = Distributions(dist="laplace", mean=2, std=3, size=25)
        self.assertEqual(dist_obj.distribution, "laplace")
        self.assertEqual(dist_obj.mean, 2)
        self.assertEqual(dist_obj.std, 3)
        self.assertEqual(dist_obj.size, 25)
        self.assertEqual(len(dist_obj.samples), 25)

    def test_unsupported_distribution(self):
        """
        Test that an unsupported distribution raises ValueError.
        """
        with self.assertRaises(ValueError):
            _ = Distributions(dist="unsupported", mean=0, std=1, size=10)

    def test_invalid_std(self):

        with self.assertRaises(ValueError):
            _ = Distributions(dist="normal", mean=0, std=-1, size=10)


class TestNumpyDistribution(unittest.TestCase):
    """
    Tests for the NumpyDistribution class (using numpy random).
    """
    def test_normal_distribution_valid_numpy(self):
        dist_obj = NumpyDistribution(dist="normal", mean=0, std=1, size=100)
        self.assertEqual(dist_obj.distribution, "normal")
        self.assertEqual(dist_obj.mean, 0)
        self.assertEqual(dist_obj.std, 1)
        self.assertEqual(dist_obj.size, 100)
        self.assertEqual(len(dist_obj.samples), 100)

    def test_lognormal_distribution_valid_numpy(self):
        dist_obj = NumpyDistribution(dist="lognormal", mean=1, std=5, size=50)
        self.assertEqual(dist_obj.distribution, "lognormal")
        self.assertEqual(dist_obj.mean, 1)
        self.assertEqual(dist_obj.std, 5)
        self.assertEqual(dist_obj.size, 50)
        self.assertEqual(len(dist_obj.samples), 50)

    def test_laplace_distribution_valid_numpy(self):
        dist_obj = NumpyDistribution(dist="laplace", mean=2, std=3, size=25)
        self.assertEqual(dist_obj.distribution, "laplace")
        self.assertEqual(dist_obj.mean, 2)
        self.assertEqual(dist_obj.std, 3)
        self.assertEqual(dist_obj.size, 25)
        self.assertEqual(len(dist_obj.samples), 25)

    def test_unsupported_distribution_numpy(self):
        with self.assertRaises(ValueError):
            _ = NumpyDistribution(dist="unsupported", mean=0, std=1, size=10)

    def test_invalid_std_numpy(self):
        with self.assertRaises(ValueError):
            _ = NumpyDistribution(dist="normal", mean=0, std=-1, size=10)


if __name__ == '__main__':
    unittest.main()