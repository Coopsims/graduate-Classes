import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

# Define the ticker symbols for the stocks
tickers = ['NVDA', 'AMD', 'AAPL', 'TSM']  # NVIDIA, AMD, Apple, Taiwan Semiconductor

# Define the date ranges
end_date_2025 = '2025-04-17'
start_date_2025 = '2025-01-01'

# Since we're currently in 2024, we'll use 2024 data for comparison with 2025
end_date_2024 = '2024-04-17'
start_date_2024 = '2024-01-01'

# Function to get stock data
def get_stock_data(ticker_list, start_date, end_date):
    data = yf.download(ticker_list, start=start_date, end=end_date, group_by='ticker')
    return data

# Get the data for 2025 and 2024
data_2025 = get_stock_data(tickers, start_date_2025, end_date_2025)
data_2024 = get_stock_data(tickers, start_date_2024, end_date_2024)

print(len(data_2025), "rows of data for 2025")
# Print the structure of the data to understand it
print("Data 2025 structure:")
print(data_2025.head())
print("\nData 2024 structure:")
print(data_2024.head())

# Process the data to ensure ticker symbol is a feature
# For MultiIndex dataframes from yfinance, we need to reset the index and restructure

# Function to process data and add Range feature
def process_data(data, year):
    # Create an empty dataframe to store processed data
    processed_data = pd.DataFrame()

    # Loop through each ticker
    for ticker in tickers:
        # Extract data for this ticker
        ticker_data = data[ticker].copy()

        # Add ticker as a column
        ticker_data['Ticker'] = ticker

        # Add year as a column
        ticker_data['Year'] = year

        # Create 'Range' feature (High - Low)
        ticker_data['Range'] = ticker_data['High'] - ticker_data['Low']

        # Add a column for day of year to align 2024 and 2025 data
        ticker_data['DayOfYear'] = ticker_data.index.dayofyear

        # Create a continuous trading day index (skipping weekends)
        ticker_data['TradingDayIndex'] = None
        trading_day_counter = 0

        for date in ticker_data.index:
            trading_day_counter += 1
            ticker_data.loc[date, 'TradingDayIndex'] = trading_day_counter

        # Append to the processed dataframe
        processed_data = pd.concat([processed_data, ticker_data])

    return processed_data

# Process both datasets
processed_2025 = process_data(data_2025, 2025)
processed_2024 = process_data(data_2024, 2024)

# Combine the datasets
combined_data = pd.concat([processed_2025, processed_2024])

# Reset index to make Date a column
combined_data = combined_data.reset_index()
combined_data = combined_data.rename(columns={'index': 'Date'})

# Print the processed data structure
print("\nProcessed data structure:")
print(combined_data.head())

# Create similar visualizations for the other stocks
for ticker in ['NVDA','AMD', 'AAPL', 'TSM']:
    plt.figure(figsize=(12, 8))

    # Select data for the current ticker
    ticker_data = combined_data[combined_data['Ticker'] == ticker]

    # Group by Year and TradingDayIndex, and calculate the mean of Close price
    ticker_grouped = ticker_data.groupby(['Year', 'TradingDayIndex'])['Close'].mean().reset_index()

    # Pivot the data to have separate columns for 2024 and 2025
    ticker_pivot = ticker_grouped.pivot(index='TradingDayIndex', columns='Year', values='Close')

    # Plot the data
    plt.plot(ticker_pivot.index, ticker_pivot[2025], label='2025', linewidth=2)
    plt.plot(ticker_pivot.index, ticker_pivot[2024], label='2024', linewidth=2)

    # Add labels and title
    plt.xlabel('Trading Day')
    plt.ylabel('Close Price (USD)')
    plt.title(f'{ticker} Stock Price Comparison: 2024 vs 2025')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    # Save the figure
    plt.savefig(f'{ticker}_stock_comparison.png', dpi=300, bbox_inches='tight')

    # Show the plot
    plt.show()

# Create a visualization of the Range feature for all stocks

# Calculate average Range by ticker and year
range_data = combined_data.groupby(['Ticker', 'Year'])['Range'].mean().reset_index()

# Pivot the data for easier plotting
range_pivot = range_data.pivot(index='Ticker', columns='Year', values='Range')

# Create a bar chart
x = np.arange(len(range_pivot.index))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(x - width/2, range_pivot[2025], width, label='2025')
ax.bar(x + width/2, range_pivot[2024], width, label='2024')

# Add labels and title
ax.set_xlabel('Stock')
ax.set_ylabel('Average Range (High - Low)')
ax.set_title('Average Daily Price Range Comparison: 2024 vs 2025')
ax.set_xticks(x)
ax.set_xticklabels(range_pivot.index)
ax.legend()

plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Save the figure
plt.savefig('stock_range_comparison.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

print("Analysis complete. Visualizations have been saved.")
