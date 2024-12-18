import requests
import pandas as pd

def fetch_market_data(api_key, symbol, start_date, end_date):
    url = f"https://api.marketdata.com/v1/{symbol}/history?start_date={start_date}&end_date={end_date}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data['prices'])
    else:
        raise ValueError("Error in fetching market data")
# Example: fetch_market_data('your_api_key', 'AAPL', '2023-01-01', '2023-12-31')
