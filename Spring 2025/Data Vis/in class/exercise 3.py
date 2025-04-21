import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [3, 1, 4, 2, 5]

df = pd.DataFrame({
    'x': x_values,
    'y': y_values
})

x_mean = df['x'].mean()
y_mean = df['y'].mean()

print(f"Mean of x: {x_mean}")
print(f"Mean of y: {y_mean}")

def assign_quadrant(row):
    if row['x'] >= x_mean and row['y'] >= y_mean:
        return 1
    elif row['x'] < x_mean and row['y'] >= y_mean:
        return 2
    elif row['x'] < x_mean and row['y'] < y_mean:
        return 3
    else:
        return 4

df['quadrant'] = df.apply(assign_quadrant, axis=1)

print("\nDataFrame with quadrant assignments:")
print(df)

plt.figure(figsize=(10, 8))

colors = {1: 'red', 2: 'blue', 3: 'green', 4: 'purple'}
for quadrant, color in colors.items():
    quadrant_data = df[df['quadrant'] == quadrant]
    plt.scatter(quadrant_data['x'], quadrant_data['y'], c=color, label=f'Quadrant {quadrant}', s=100)

plt.axvline(x=x_mean, color='black', linestyle='--', alpha=0.7)
plt.axhline(y=y_mean, color='black', linestyle='--', alpha=0.7)

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot')
plt.grid(True, alpha=0.3)
plt.legend()

plt.text(x_mean + 0.1, y_mean + 0.1, "Q1", fontsize=12)
plt.text(x_mean - 0.5, y_mean + 0.1, "Q2", fontsize=12)
plt.text(x_mean - 0.5, y_mean - 0.3, "Q3", fontsize=12)
plt.text(x_mean + 0.1, y_mean - 0.3, "Q4", fontsize=12)

plt.text(x_mean + 0.1, y_mean - 0.1, f"x_mean = {x_mean:.2f}", fontsize=10)
plt.text(x_mean - 0.5, y_mean - 0.1, f"y_mean = {y_mean:.2f}", fontsize=10)

# plt.tight_layout()
plt.show()