# %% [markdown]
# # Data Visualization - Assignment 2: Pair Plot Analysis
# 
# This notebook contains the implementation of a custom pair plot for the diamonds dataset from Seaborn.

# %% [markdown]
# ## Import Libraries

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plots
plt.style.use('seaborn-v0_8-whitegrid')

# %% [markdown]
# ## Load the Diamonds Dataset
# 
# As per the assignment instructions, we'll load the diamonds dataset from Seaborn.

# %%
# Load the diamonds dataset from Seaborn
diamonds = sns.load_dataset('diamonds')

# Display the first few rows of the dataset
diamonds.head()

# %% [markdown]
# ## Explore the Dataset
# 
# Let's explore the dataset to understand its structure and identify continuous variables.

# %%
# Get information about the dataset
print("Dataset Information:")
print(f"Number of rows: {diamonds.shape[0]}")
print(f"Number of columns: {diamonds.shape[1]}")
print("\nColumn Data Types:")
print(diamonds.dtypes)

# %%
# Get summary statistics for numerical columns
diamonds.describe()

# %% [markdown]
# Based on the dataset exploration, we can identify several continuous variables:
# - carat: weight of the diamond
# - depth: total depth percentage
# - table: width of top of diamond relative to widest point
# - price: price in US dollars
# - x: length in mm
# - y: width in mm
# - z: depth in mm
# 
# For our pair plot, we'll select three of these continuous variables: carat, price, and depth.

# %% [markdown]
# ## Implement Custom Pair Plot
# 
# Now we'll implement a custom pair plot with the following features:
# - 3x3 subplot grid for our three selected variables
# - Histograms on the diagonal with custom binning
# - Scatter plots on the off-diagonal
# - Different shades of gray for scatter plots above and below the diagonal
# - Appropriate labels and title

# %%
# Select the three continuous variables for our pair plot
selected_vars = ['carat', 'price', 'depth']
selected_data = diamonds[selected_vars]

# Create descriptive names for the variables
var_names = {
    'carat': 'Weight',
    'price': 'Price',
    'depth': 'Depth Percentage'
}

# %%
# Create a function to implement a custom pair plot
def custom_pair_plot(data, var_names, fig_size=(12, 12)):
    """
    Create a custom pair plot for the given data.

    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the variables to plot
    var_names : dict
        Dictionary mapping variable names to descriptive names
    fig_size : tuple, optional
        Figure size (width, height) in inches
    """
    # Get the variable names
    vars_to_plot = list(data.columns)
    n_vars = len(vars_to_plot)

    # Create a figure with a grid of subplots
    fig, axes = plt.subplots(n_vars, n_vars, figsize=fig_size)

    # Define gray shades for scatter plots
    light_gray = '0.7'  # Light gray for plots above diagonal
    dark_gray = '0.3'   # Dark gray for plots below diagonal

    # Loop through each variable pair
    for i, var_i in enumerate(vars_to_plot):
        for j, var_j in enumerate(vars_to_plot):
            ax = axes[i, j]

            # Diagonal: Histogram with custom binning
            if i == j:
                # Get the data for the current variable
                x = data[var_i]

                # Implement custom binning using Freedman-Diaconis rule
                # This rule estimates optimal bin width as 2 * IQR(x) / (n^(1/3))
                q75, q25 = np.percentile(x, [75, 25])
                iqr = q75 - q25
                bin_width = 2 * iqr / (len(x) ** (1/3))
                n_bins = int(np.ceil((x.max() - x.min()) / bin_width))

                # Create the histogram
                ax.hist(x, bins=n_bins, color='gray', alpha=0.7, edgecolor='black')

                # Add a title with the descriptive variable name
                ax.set_title(var_names[var_i])

                # Remove y-axis labels for cleaner look
                ax.set_yticklabels([])

            # Off-diagonal: Scatter plots
            else:
                # Get the data for the current variable pair
                x = data[var_j]
                y = data[var_i]

                # Choose color based on position relative to diagonal
                color = light_gray if i < j else dark_gray

                # Create the scatter plot
                ax.scatter(x, y, s=5, color=color, alpha=0.6)

                # Add a title with descriptive variable names
                if i == 0:  # Top row
                    ax.set_title(var_names[var_j])
                if j == 0:  # First column
                    ax.set_ylabel(var_names[var_i])

                # Add a more descriptive title inside the plot
                if i != 0 or j != 0:  # Skip the top-left plot
                    ax.set_title(f"{var_names[var_i]} by {var_names[var_j]}", 
                                fontsize=8, pad=2)

    # Add a main title to the figure
    fig.suptitle('Pair Plot of Diamond Characteristics', fontsize=16, y=0.98)

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)

    return fig, axes

# %%
# Create the custom pair plot
fig, axes = custom_pair_plot(selected_data, var_names)

# Display the plot
plt.show()

# %% [markdown]
# ## Observations on Variable Distributions and Relationships
# 
# From the pair plot above, we can observe several interesting patterns in the diamond dataset. The carat (weight) distribution is right-skewed, indicating that smaller diamonds are more common in the market. Price follows a similar right-skewed distribution, with most diamonds falling in the lower price range. Depth percentage shows a more normal distribution centered around 61-62%. There's a strong positive correlation between carat and price, which is expected as larger diamonds typically cost more. The relationship between depth and the other variables is less pronounced, suggesting that depth percentage is not as strongly related to either weight or price as they are to each other.
