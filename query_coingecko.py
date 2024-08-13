import requests
import pandas as pd
def fetch_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1, "sparkline": "false"}
    response = requests.get(url, params=params)
    data = response.json()
    return data
def process_data(data):
    df = pd.DataFrame(data)
    stats = df.describe()
    df.to_csv("coingecko_data.csv", index=False)
    stats.to_csv("coingecko_stats.csv")
    return stats
if __name__ == "__main__":
    data = fetch_data()
    stats = process_data(data)
    print("Estadísticas guardadas en coingecko_stats.csv")
