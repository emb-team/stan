import get_tickers as gt
import yfinance as yf
import logging


def get_hist_and_anal(ticker):

    stock = yf.Ticker(ticker)
    if stock is None:
        return

    # get historical market data
    hist = stock.history(period="5d")
    if hist is None:
        return

    #today=date.today()
    #start=today-timedelta(days=3)

    prices=hist["Close"]
    if prices is None:
        return

    if prices.size >= 5:
        reduc=prices.values[0]*15/100
        target =prices.values[0] - reduc
        if prices.values[4] <= target:
            print("--------------------------------------");
            print("Ticker: " + ticker)
            print("https://finance.yahoo.com/quote/" + ticker + "/")
            print(type(prices))
            print(prices)
            print(stock.financials)
    else:
        return


logger = logging.getLogger("yfinance")
logging.basicConfig(level=logging.CRITICAL)

#tickers = gt.get_tickers()

# tickers from NASDAQ only
gt._EXCHANGE_LIST = ['nasdaq']

filtered_by_sector = gt.get_tickers_filtered(mktcap_min=2000)
#, sectors=[gt.SectorConstants.TECH, gt.SectorConstants.FINANCE])
yf.download(filtered_by_sector,period="5d")
for ticker in filtered_by_sector:
    get_hist_and_anal(ticker)
