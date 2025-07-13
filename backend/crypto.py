import requests

class CryptoMarketInterface:
    BASE_URL = "https://api.coingecko.com/api/v3"

    def get_price(self, symbol: str, currency: str = "usd") -> float | None:
        """
        Get the current price of a cryptocurrency.
        :param symbol: The coin symbol (e.g., 'bitcoin', 'ethereum')
        :param currency: The fiat currency (default: 'usd')
        :return: Current price as a float, or None if an error occurs.
        """
        url = f"{self.BASE_URL}/simple/price"
        params = {"ids": symbol, "vs_currencies": currency}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            data = response.json()
            price = data.get(symbol, {}).get(currency)
            if price is None:
                print(f"Warning: Could not find price for {symbol} in {currency}")
            return price
        except requests.exceptions.RequestException as e:
            print(f"An error occurred fetching price: {e}")
            return None

    def get_market_data(self, symbol: str) -> dict | None:
        """
        Get market data for a cryptocurrency.
        :param symbol: The coin symbol (e.g., 'bitcoin')
        :return: Market data as dict, or None if an error occurs.
        """
        url = f"{self.BASE_URL}/coins/{symbol}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred fetching market data: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    market = CryptoMarketInterface()
    price = market.get_price("bitcoin")
    if price is not None:
        print(f"Bitcoin price (USD): {price}")

    market_data = market.get_market_data("bitcoin")
    if market_data:
        print(f"Bitcoin market data available for keys: {market_data.keys()}")

