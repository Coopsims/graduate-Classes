import random

import numpy as np
import matplotlib.pyplot as plt

mu = 100
sig = 50

n = [random.gauss(mu, sig) for i in range(10000)]

plt.hist(n, bins=100)
plt.show()