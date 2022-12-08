"""
How to run the app
# Dependencies
pip install streamlit
pip install binance
pip install pandas

# Run the app
streamlit run app.py
"""


import streamlit as st
# from binance import Client
import pandas as pd

st.markdown('''# **Crypto Price App powered by Binance API**
Simple UI displaying crypto prices using streamlit powered by Binance API.
''')

# Load market data from Binance API
df = pd.read_json('https://api.binance.us/api/v3/ticker/24hr')

# Print out all prices
st.header('**All Prices**')
# Display the datafram on streamlit
st.dataframe(df)
tickers = ['BTCUSDT','XRPUSDT',
 'TRXUSDT',
 'WAVESUSDT',
 'ZILUSDT',
 'ONEUSDT',
 'COTIUSDT',
 'SOLUSDT',
 'EGLDUSDT',
 'AVAXUSDT',
 'NEARUSDT',
 'FILUSDT',
 'AXSUSDT',
 'ROSEUSDT',
 'ARUSDT',
 'MBOXUSDT',
 'YGGUSDT',
 'BETAUSDT',
 'PEOPLEUSDT',
 'EOSUSDT',
 'ATOMUSDT',
 'FTMUSDT',
 'DUSKUSDT',
 'IOTXUSDT',
 'OGNUSDT',
 'CHRUSDT',
 'MANAUSDT',
 'XEMUSDT',
 'SKLUSDT',
 'ICPUSDT',
 'FLOWUSDT',
 'WAXPUSDT',
 'FIDAUSDT',
 'ENSUSDT',
 'SPELLUSDT',
 'LTCUSDT',
 'IOTAUSDT',
 'LINKUSDT',
 'XMRUSDT',
 'DASHUSDT',
 'MATICUSDT',
 'ALGOUSDT',
 'ANKRUSDT',
 'COSUSDT',
 'KEYUSDT',
 'XTZUSDT',
 'RENUSDT',
 'RVNUSDT',
 'HBARUSDT',
 'BCHUSDT',
 'COMPUSDT',
 'ZENUSDT',
 'SNXUSDT',
 'SXPUSDT',
 'SRMUSDT',
 'SANDUSDT',
 'SUSHIUSDT',
 'YFIIUSDT',
 'KSMUSDT',
 'DIAUSDT',
 'RUNEUSDT',
 'AAVEUSDT',
 '1INCHUSDT',
 'ALICEUSDT',
 'FARMUSDT',
 'REQUSDT',
 'GALAUSDT',
 'POWRUSDT',
 'OMGUSDT',
 'DOGEUSDT',
 'SCUSDT',
 'XVSUSDT',
 'ASRUSDT',
 'CELOUSDT',
 'RAREUSDT',
 'ADXUSDT',
 'CVXUSDT',
 'WINUSDT',
 'C98USDT',
 'FLUXUSDT',
 'ENJUSDT',
 'FUNUSDT',
 'KP3RUSDT',
 'ALCXUSDT',
 'ETCUSDT',
 'THETAUSDT',
 'CVCUSDT',
 'STXUSDT',
 'CRVUSDT',
 'MDXUSDT',
 'DYDXUSDT',
 'OOKIUSDT',
 'CELRUSDT',
 'RSRUSDT',
 'ATMUSDT',
 'LINAUSDT',
 'POLSUSDT',
 'ATAUSDT',
 'RNDRUSDT',
 'NEOUSDT',
 'ALPHAUSDT',
 'XVGUSDT',
 'KLAYUSDT',
 'DFUSDT',
 'VOXELUSDT',
 'LSKUSDT',
 'KNCUSDT',
 'NMRUSDT',
 'MOVRUSDT',
 'PYRUSDT',
 'ZECUSDT',
 'CAKEUSDT',
 'HIVEUSDT',
 'UNIUSDT',
 'SYSUSDT',
 'BNXUSDT',
 'GLMRUSDT',
 'LOKAUSDT',
 'CTSIUSDT',
 'REEFUSDT',
 'AGLDUSDT',
 'MCUSDT',
 'ICXUSDT',
 'TLMUSDT',
 'MASKUSDT',
 'IMXUSDT',
 'XLMUSDT',
 'BELUSDT',
 'HARDUSDT',
 'NULSUSDT',
 'TOMOUSDT',
 'NKNUSDT',
 'BTSUSDT',
 'LTOUSDT',
 'STORJUSDT',
 'ERNUSDT',
 'XECUSDT',
 'ILVUSDT',
 'JOEUSDT',
 'SUNUSDT',
 'ACHUSDT',
 'TROYUSDT',
 'YFIUSDT',
 'CTKUSDT',
 'BANDUSDT',
 'RLCUSDT',
 'TRUUSDT',
 'MITHUSDT',
 'AIONUSDT',
 'ORNUSDT',
 'WRXUSDT',
 'WANUSDT',
 'CHZUSDT',
 'ARPAUSDT',
 'LRCUSDT',
 'IRISUSDT',
 'UTKUSDT',
 'QTUMUSDT',
 'GTOUSDT',
 'MTLUSDT',
 'KAVAUSDT',
 'DREPUSDT',
 'OCEANUSDT',
 'UMAUSDT',
 'FLMUSDT',
 'UNFIUSDT',
 'BADGERUSDT',
 'PONDUSDT',
 'PERPUSDT',
 'TKOUSDT',
 'GTCUSDT',
 'TVKUSDT',
 'MINAUSDT',
 'RAYUSDT',
 'LAZIOUSDT',
 'AMPUSDT',
 'BICOUSDT',
 'CTXCUSDT',
 'FISUSDT',
 'BTGUSDT',
 'TRIBEUSDT',
 'QIUSDT',
 'PORTOUSDT',
 'DATAUSDT',
 'NBSUSDT',
 'EPSUSDT',
 'TFUELUSDT',
 'BEAMUSDT',
 'REPUSDT',
 'PSGUSDT',
 'WTCUSDT',
 'FORTHUSDT',
 'BONDUSDT',
 'ZRXUSDT',
 'FIROUSDT',
 'SFPUSDT',
 'VTHOUSDT',
 'FIOUSDT',
 'PERLUSDT',
 'WINGUSDT',
 'AKROUSDT',
 'BAKEUSDT',
 'ALPACAUSDT',
 'FORUSDT',
 'IDEXUSDT',
 'PLAUSDT',
 'VITEUSDT',
 'DEGOUSDT',
 'XNOUSDT',
 'STMXUSDT',
 'JUVUSDT',
 'STRAXUSDT',
 'CITYUSDT',
 'JASMYUSDT',
 'DEXEUSDT',
 'OMUSDT',
 'MKRUSDT',
 'FXSUSDT',
 'ETHUSDT',
 'ADAUSDT',
'BNBUSDT',
'SHIBUSDT']

# This variable will equal the symbol you chose
dropdown = st.selectbox("Pick your coin", tickers)
# Dataframe of one ticker
oneTicker = df[df['symbol'] == dropdown]
# Index of the ticker to pick values later
index = df[df['symbol']==dropdown].index.values.astype(int)[0]
st.dataframe(oneTicker)

# Creating row in website
with st.container():
    # Creating columns and displaying attributes in columns
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.markdown('### **Price Change**')
        st.markdown('**' + str(oneTicker.loc[index].at['priceChange']) + '**')
    with col2:
        st.markdown('### **Price Change Percent**')
        st.markdown('**' + str(oneTicker.loc[index].at['priceChangePercent']) + '%**')
    with col3: 
        st.markdown('### **Weighted Average Price**')
        st.markdown('**' + str(oneTicker.loc[index].at['weightedAvgPrice']) + '**')
    with col4:
        st.markdown('### **Previous Close Price**')
        st.markdown('**' + str(oneTicker.loc[index].at['prevClosePrice']) + '**')
    with col5:
        st.markdown('### **High Price**')
        st.markdown('**' + str(oneTicker.loc[index].at['highPrice']) + '**')
    with col6:
        st.markdown('### **Low Price**')
        st.markdown('**' + str(oneTicker.loc[index].at['lowPrice']) + '**')


# Data frames we will use 
tickerDF = pd.read_json('https://api.binance.us/api/v3/ticker/24hr')
# Sort dataframe for gain loss
tickerDF = tickerDF.sort_values('priceChangePercent')
# Subset of data frame with symbol and volume
tickerSubsetDF = tickerDF[['symbol', 'volume']]

# Code to create bar chart
# Print out the header
st.header('**Volume Bar Chart**')
# Finding the tickers with the highest 
tickerSubsetDF = tickerSubsetDF.sort_values('volume')
tickerSubsetLast10 = tickerSubsetDF.tail(10)
st.bar_chart(tickerSubsetLast10, x='symbol', y='volume')


# Side bar features
# Print 10 stocks with the highest gain percent
st.sidebar.markdown("# **Top Gainers**")
for i in range(10):
    st.sidebar.markdown('### **' + tickerDF.loc[i].at['symbol'] + '**')
    st.sidebar.markdown(str(tickerDF.loc[i].at['priceChangePercent']) + '%')
    

# Print 10 stocks with the lowest gain percent
st.sidebar.markdown("# **Top Losers**")
for i in range(len(tickerDF)-1, len(tickerDF)-11, -1):
    st.sidebar.markdown('### **' + tickerDF.loc[i].at['symbol'] + '**')
    st.sidebar.markdown(str(tickerDF.loc[i].at['priceChangePercent']) + '%')
