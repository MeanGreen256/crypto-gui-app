# Crypto Price Viewer

This is a simple desktop application built with Python and Tkinter that displays and plots the price of Bitcoin.

## Features

*   Fetches the current price of Bitcoin.
*   Plots the historical price of Bitcoin over a selectable time range (7, 30, or 90 days).
*   Simple and easy-to-use graphical user interface.

## Dependencies

The application requires the following Python libraries:

*   `requests`: For making HTTP requests to the CoinGecko API.
*   `matplotlib`: For plotting the price chart.

You will also need a working Python 3 installation with Tkinter, which is usually included by default.

## Installation

1.  Clone this repository or download the source code.
2.  Navigate to the project directory.
3.  It is recommended to use a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```
4.  Install the required packages:
    ```bash
    pip install requests matplotlib
    ```

## How to Run

To start the application, run the `crypto_test.py` script from within the `src` directory:

```bash
python src/crypto_test.py
```

The application window will appear, and it will fetch and display the Bitcoin price and plot for the last 30 days by default. You can select a different time range and click the button to refresh the data.