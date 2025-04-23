import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the DataFrame
data = {
    'Automobile': ['Toyota Camry', 'Dacia Sandero', 'Fiat Panda', 'Reliant Robin', 'Tesla Model 3'],
    'Units Sold': [4000, 15000, 10000, 9500, 2]
}
df = pd.DataFrame(data)

# Step 2: Pie chart (quantities as percentages)
plt.figure(figsize=(6, 6))
plt.pie(df['Units Sold'], labels=df['Automobile'], autopct='%1.1f%%', startangle=140)
plt.title('Cars Units Sales Distribution Across Denver')
plt.tight_layout()
plt.show()

# Step 3: Vertical Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df['Automobile'], df['Units Sold'], color='skyblue')
plt.ylabel('Units Sold')
plt.title('Units Sold by Car')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 4: Horizontal Bar Chart
plt.figure(figsize=(8, 5))
plt.barh(df['Automobile'], df['Units Sold'], color='salmon')
plt.xlabel('Units Sold')
plt.title('Units Sold by Car')
plt.tight_layout()
plt.show()