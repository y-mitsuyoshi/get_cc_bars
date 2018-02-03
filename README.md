## sample  

```python
start = "1 Dec, 2017"  
end = "1 Jan, 2018"  
bar_duration = "1d"  

bi = Binance(api_key, api_secret)  
bi.get_bars(bar_duration, start, end)  
```

#bar_duration_list
#['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M']
# get_cc_bars
