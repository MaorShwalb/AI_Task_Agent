import yfinance as yf

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")

    if data.empty:
        return None

    latest = data.iloc[-1]

    return {
        "price": latest["Close"],
        "open": latest["Open"],
        "high": latest["High"],
        "low": latest["Low"]
    }