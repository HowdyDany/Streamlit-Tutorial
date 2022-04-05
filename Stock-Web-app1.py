# This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time
import yfinance as yf
#---------------------------------#
# New feature (make sure to upgrade your streamlit library)
# pip install --upgrade streamlit

#---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(layout="wide")
#---------------------------------#
# Title


st.write( """
Stock Application
""")
Symbol = st.text_input("Enter your favorite stock", 'AAPL')
Data = yf.Ticker(Symbol)
end = time.strftime("%Y-%m-%d")
df = Data.history(period='1d', start='2015-01-01', end=end)
st.line_chart(df.Close)
st.line_chart(df.Volume)
st.table(df.tail())







