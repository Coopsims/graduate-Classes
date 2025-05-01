import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import warnings

warnings.simplefilter("ignore", RuntimeWarning)

# Data sets
datasets = [
    {
        "x": np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        "y": np.array([3.277, 3.129, 5.415, 9.763, 15.397, 23.844, 33.958, 45.554, 59.140, 75.245]),
        "name": "Dataset 1"
    },
    {
        "x": np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        "y": np.array([0.675, 2.226, 4.283, 6.536, 8.488, 11.600, 13.769, 17.252, 19.872, 23.728]),
        "name": "Dataset 2"
    },
    {
        "x": np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        "y": np.array([1.846, 6.976, 19.511, 42.244, 78.112, 126.516, 191.826, 275.225, 377.709, 501.987]),
        "name": "Dataset 3"
    }
]

# Curve functions
def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

def poly3(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

def power_func(x, a, b, c):
    return a * (x) ** b + c

def log_func(x, a, b, c):
    return a * x * np.log(b*x) + c

functions_to_try = [
    (poly2, "Quadratic"),
    (poly3, "Cubic"),
    (power_func, "Power"),
    (log_func, "Logarithmic"),
]

for dataset in datasets:
    x_data = dataset["x"]
    y_data = dataset["y"]
    results = []

    plt.figure(figsize=(8, 5))
    plt.scatter(x_data, y_data, label='Data', color='black')

    x_fit = np.linspace(x_data.min(), x_data.max(), 100)

    for func, desc in functions_to_try:
        try:
            popt, _ = curve_fit(func, x_data, y_data, maxfev=10000)
            residuals = y_data - func(x_data, *popt)
            ss_res = np.sum(residuals ** 2)
            results.append((ss_res, desc, popt, func))
            plt.plot(x_fit, func(x_fit, *popt), label=f"{desc} (SSR={ss_res:.2f})")
        except Exception:
            pass

    results.sort(key=lambda tup: tup[0])
    best = results[0]
    plt.title(f'{dataset["name"]}\nBest fit: {best[1]}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.tight_layout()
    plt.show()
    print(f"\n{dataset['name']} - Best fit: {best[1]}, Params: {best[2]}, SSR: {best[0]:.4f}")