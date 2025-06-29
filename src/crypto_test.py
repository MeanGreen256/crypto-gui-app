import tkinter as tk
import requests
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_and_plot_bitcoin_data():
    try:
        # Get the selected time range from the radio buttons
        days = time_range_var.get()

        # Fetch historical data for the selected time range
        params = {'vs_currency': 'usd', 'days': str(days), 'interval': 'daily'}
        response = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart", params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()

        prices = data.get('prices', [])
        if not prices:
            price_label.config(text="Error: No price data found.")
            return

        from matplotlib.dates import date2num

        timestamps = [datetime.fromtimestamp(p[0] / 1000) for p in prices]
        price_values = [p[1] for p in prices]

        latest_price = price_values[-1]
        price_label.config(text=f"Bitcoin Price: ${latest_price:,.2f}")
        print(f"Bitcoin Price: ${latest_price:,.2f}")  # Print to console for debugging

        # Convert datetime objects to matplotlib date numbers
        date_nums = date2num(timestamps)

        # Clear the axes and redraw the plot
        ax.clear()
        ax.plot(date_nums, price_values)
        ax.set_title(f"Bitcoin Price (Last {days} Days)")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        fig.autofmt_xdate()
        ax.grid(True)
        canvas.draw()

    except requests.exceptions.RequestException as e:
        price_label.config(text=f"Error: Could not fetch data. {e}")
    except Exception as e:
        price_label.config(text=f"An error occurred: {e}")

# Set up the main window
root = tk.Tk()
root.title("Bitcoin Price Tracker")

# --- Time Range Selection ---
time_range_frame = tk.Frame(root)
time_range_frame.pack(pady=5)

tk.Label(time_range_frame, text="Select Time Range:").pack(side=tk.LEFT, padx=5)

time_range_var = tk.IntVar(value=30)  # Default to 30 days

tk.Radiobutton(time_range_frame, text="7 Days", variable=time_range_var, value=7).pack(side=tk.LEFT)
tk.Radiobutton(time_range_frame, text="30 Days", variable=time_range_var, value=30).pack(side=tk.LEFT)
tk.Radiobutton(time_range_frame, text="90 Days", variable=time_range_var, value=90).pack(side=tk.LEFT)

# Create and place widgets
fetch_button = tk.Button(root, text="Get Bitcoin Price and Plot", command=get_and_plot_bitcoin_data)
fetch_button.pack(pady=10)

price_label = tk.Label(root, text="Bitcoin Price: N/A", font=("Arial", 16))
price_label.pack()

# --- Matplotlib Plot Setup ---
fig, ax = plt.subplots(figsize=(10, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Initial data fetch
get_and_plot_bitcoin_data()

# Start the main loop
root.mainloop()
