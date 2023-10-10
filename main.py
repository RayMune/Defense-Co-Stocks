# Import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt

# Define a list of stock symbols
stocks = ["LMT", "NOC", "BA", "BAESY", "RTX", "GD"]

# Create an empty DataFrame to store opening prices
opening_prices = {}

# Define the date range
start_date = "2023-10-01"
end_date = "2023-10-09"

# Loop through each stock symbol
for symbol in stocks:
    # Download the stock data for the specified date range
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    
    # Extract the opening prices
    opening_prices[symbol] = stock_data["Open"]

# Create a DataFrame from the opening_prices dictionary
opening_prices_df = pd.DataFrame(opening_prices)

# Plot the data
plt.figure(figsize=(12, 6))
for symbol in stocks:
    plt.plot(opening_prices_df.index, opening_prices_df[symbol], label=symbol)

# Add labels and title
plt.xlabel("Date")
plt.ylabel("Opening Price")
plt.title("Opening Prices Comparison - Oct 1st vs. Oct 9th, 2023")

# Add legend
plt.legend()

# Show the plot
plt.show()
