import streamlit as stream
import yfinance as yf

ticker_symbol = 'PAYC'

stream.write("""
# Simple Stock Price App

""")

ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period='1m', start="2010-5-31", end="2020-5-31")

print(ticker_df)
stream.line_chart(ticker_df.Close)

stream.line_chart(ticker_df.Volume)

#print(data)