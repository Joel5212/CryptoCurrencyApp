import streamlit as st
import pandas as pd

st.markdown('''# **Crypto Price App powered by Binance API**
Simple UI displaying crypto prices using streamlit powered by Binance API.
''')

st.header('**Selected Price**')

# Load market data from Binance API
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

st.header('**All Prices**')
st.dataframe(df)