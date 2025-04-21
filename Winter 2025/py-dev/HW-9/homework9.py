# Imports
import random
import math
import numpy as np
import matplotlib.pyplot as plt


class Distributions:
    """
    A class to represent different probability distributions using the built-in 'random' module.
    """

    def __init__(self, dist, mean, std, size):
        """
        Constructor for Distributions class.

        Args:
            dist (str): Specifies which distribution to generate.
            mean (float): Mean of the chosen distribution.
            std (float): Standard deviation of the chosen distribution.
            size (int): Number of samples to generate.

        Returns:
            Distributions object.
        """
        if std <= 0:
            raise ValueError("Standard deviation must be positive.")
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        self.distribution = dist.lower()
        self.mean = mean
        self.std = std
        self.size = size
        # Generate the samples
        self.samples = self._generate_samples()

    def __str__(self):
        """
        String representation of the distribution object.

        Returns:
            str: Human-readable string describing the distribution.
        """
        return (f"Distributions("
                f"distribution='{self.distribution}', "
                f"mean={self.mean}, "
                f"std={self.std}, "
                f"size={self.size})")

    def _generate_samples(self):
        """
        Generate samples based on the specified distribution.

        Returns:
            list: A list containing generated samples.
        """
        if self.distribution == 'normal':
            return [random.gauss(self.mean, self.std) for _ in range(self.size)]

        elif self.distribution == 'lognormal':
            # Interpreting mean, std as mu, sigma in the log space
            return [random.lognormvariate(self.mean, self.std) for _ in range(self.size)]

        elif self.distribution == 'laplace':
            # There's no built-in Laplace generator in random, so we do inverse transform.
            b = self.std / math.sqrt(2)
            samples = []
            for _ in range(self.size):
                U = random.random()
                if U < 0.5:
                    x = self.mean + b * math.log(2 * U)
                else:
                    x = self.mean - b * math.log(2 * (1 - U))
                samples.append(x)
            return samples

        else:
            raise ValueError("Unsupported distribution. Choose 'normal', 'lognormal', or 'laplace'.")


class NumpyDistribution:
    """
    A class to represent different probability distributions using numpy.
    """


    def __init__(self, dist, mean, std, size):
        """
        Constructor for NumpyDistribution class.

        Args:
            dist (str): Specifies which distribution to generate.
            mean (float): Mean of the chosen distribution.
            std (float): Standard deviation of the chosen distribution.
            size (int): Number of samples to generate.

        Returns:
            NumpyDistribution object.
        """
        if std <= 0:
            raise ValueError("Standard deviation must be positive.")
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        self.distribution = dist.lower()
        self.mean = mean
        self.std = std
        self.size = size
        self.samples = self._generate_samples()

    def __str__(self):
        """
        String representation of distribution object.

        Returns:
            str: Human-readable string describing distribution.
        """
        return (f"NumpyDistribution("
                f"distribution='{self.distribution}', "
                f"mean={self.mean}, "
                f"std={self.std}, "
                f"size={self.size})")

    def _generate_samples(self):
        """
        Generate samples based on specified distribution using numpy.

        Returns:
            numpy.ndarray: An array containing generated samples.
        """
        if self.distribution == 'normal':
            return np.random.normal(self.mean, self.std, self.size)

        elif self.distribution == 'lognormal':
            return np.random.lognormal(self.mean, self.std, self.size)

        elif self.distribution == 'laplace':
            scale_param = self.std / np.sqrt(2)
            return np.random.laplace(self.mean, scale_param, self.size)

        else:
            raise ValueError("Unsupported distribution. Choose 'normal', 'lognormal', or 'laplace'.")


def plot_sine_cosine_same_axes():
    """
    Plots one period of sine and cosine on same axes.
    """
    x_values = np.linspace(0, 2 * np.pi, 300)
    plt.plot(x_values, np.sin(x_values), label='Sine')
    plt.plot(x_values, np.cos(x_values), label='Cosine')
    plt.title("Sine and Cosine on the Same Axes")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_sine_cosine_different_axes_share_y():
    """
    Plots one period of sine and cosine on different axes, sharing y-axis.
    """
    x_values = np.linspace(0, 2 * np.pi, 300)
    fig, axes = plt.subplots(1, 2, sharey=True)
    fig.suptitle("Sine and Cosine on Different Axes (Shared Y-axis)")

    axes[0].plot(x_values, np.sin(x_values), label='Sine')
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("f(x)")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].plot(x_values, np.cos(x_values), label='Cosine')
    axes[1].set_xlabel("x")
    axes[1].grid(True)
    axes[1].legend()

    plt.show()


def plot_sine_cosine_different_axes_share_x():
    """
    Plots one period of sine and cosine on different axes, sharing x-axis.
    """
    x_values = np.linspace(0, 2 * np.pi, 300)
    fig, axes = plt.subplots(2, 1, sharex=True)
    fig.suptitle("Sine and Cosine on Different Axes (Shared X-axis)")

    axes[0].plot(x_values, np.sin(x_values), label='Sine')
    axes[0].set_ylabel("f(x)")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].plot(x_values, np.cos(x_values), label='Cosine')
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("f(x)")
    axes[1].grid(True)
    axes[1].legend()

    plt.show()


def main():
    # Quick test of Distributions
    dist_obj = Distributions(dist="normal", mean=0, std=1, size=10)
    print(dist_obj)
    print("First 5 samples:", dist_obj.samples[:5])

    # Quick test of NumpyDistribution
    np_dist_obj = NumpyDistribution(dist="laplace", mean=0, std=1, size=10)
    print(np_dist_obj)
    print("First 5 samples (Numpy):", np_dist_obj.samples[:5])

    # Plotting
    plot_sine_cosine_same_axes()
    plot_sine_cosine_different_axes_share_y()
    plot_sine_cosine_different_axes_share_x()


if __name__ == '__main__':
    main()