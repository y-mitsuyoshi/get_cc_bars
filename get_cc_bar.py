from binance.client import Client
from datetime import datetime

class Binance(object):
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def get_bars(self, bar_duration, start, end):
        kline_list = []
        for ticker_combination in self.ticker_combinations():    
            klines = self.client.get_historical_klines(ticker_combination, bar_duration, start, end)
            klines = self.format_klines(klines)
            kline_list.append({"ticker_combination":ticker_combination, "klines":klines})
        return kline_list

    def ticker_combinations(self):        
        combinations = self.client.get_all_tickers()
        ticker_combination_list = []
        for combination in combinations:
            ticker_combination_list.append(combination['symbol'])
        return ticker_combination_list

    def format_klines(self, klines):
        klines = list(map(lambda x: [self.format_timestamp(x[0]),x[1],x[2],x[3],x[4],x[5],self.format_timestamp(x[6]),x[7],x[8],x[9],x[10],x[11]], klines))
        return klines

    def format_timestamp(self, timestamp):
        time = datetime.fromtimestamp(timestamp/1000)
        return time

