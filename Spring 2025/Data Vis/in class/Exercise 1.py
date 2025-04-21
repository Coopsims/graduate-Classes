import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1001)

y_sin = np.sin(x)
y_cos = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))

ax1.plot(x, y_sin, label='sin(x)', color='blue')
ax1.set_title('Sine')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)
ax1.legend()

ax2.plot(x, y_cos, label='cos(x)', color='red')
ax2.set_title('Cosine')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.grid(True)
ax2.legend()

fig.tight_layout()
plt.show()
