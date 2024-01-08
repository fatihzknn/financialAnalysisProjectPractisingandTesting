import pandas as pd
import yfinance as yf
from datetime import datetime


stock = "AAPL"

# time
start_date = datetime(2012, 2, 2)
end_date = datetime.today()

# yfinance data pullling
bist30_data = yf.download(stock, start=start_date, end=end_date)
usd_try_data = yf.download("USDTRY=X", start=start_date, end=end_date)
brent_data = yf.download("BZ=F", start=start_date, end=end_date)
closeThyao = bist30_data["Close"]
closeUsd = usd_try_data["Close"]
closeBrent = brent_data["Close"]
bist30_data["Usd"] = closeUsd
bist30_data["Brent"]= closeBrent
bist30_data.fillna(method= "ffill" ,inplace = True)

bist30_data = bist30_data[["Close","Brent","Usd","Volume"]]


# print(bist30_data.tail())
# print(bist30_data.tail())
