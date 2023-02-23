import yfinance as yf


def get_stock_LTP(symbol):
    symbol = symbol+".NS"
    stock = yf.Ticker(symbol)
    print(stock.fast_info["lastPrice"])
    return {    
  "last_price": stock.fast_info["lastPrice"]
}
   



