import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
from datetime import datetime
from datetime import timedelta, date
import pickle
import streamlit_authenticator as stauth
from pathlib import Path

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

current_dateTime = datetime.now()

st.set_page_config(
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    theme="dark",
)

imageLOGO = Image.open(urlopen("https://i.ibb.co/mhwTKWs/sboy-logo.png"))
st.image(imageLOGO)
st.markdown("")
logo = Image.open(urlopen("https://i.ibb.co/wpKzc3j/twitter.png"))
st.image(logo)

st.write("[Follow me on Twitter](https://twitter.com/sboy_06)")


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.header("Volume & Price Analysis")

st.sidebar.success("Select which tool you want to use")

Bitcoin = "BTC-USD"
Ethereum = "ETH-USD"
Polkadot = "DOT-USD"
Cosmos = "ATOM-USD"
Quant = "QNT-USD"
HEX = "HEX-USD"
Solana = "SOL-USD"
Avalanche = "AVAX-USD"
#Cardano = "ADA-USD"
#Polygon = "MATIC-USD"
#Uniswap = "UNI-USD"
#Doge = "DOGE-USD"

Tesla = "TSLA"
AAPL = "AAPL"
Amazon = "AMZN"
Google = "GOOGL"

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
DOT_Data = yf.Ticker(Polkadot)
ATOM_Data = yf.Ticker(Cosmos)
QNT_Data = yf.Ticker(Quant)
HEX_Data = yf.Ticker(HEX)
SOL_Data = yf.Ticker(Solana)
AVAX_Data = yf.Ticker(Avalanche)
TSLA_Data = yf.Ticker(Tesla)
AAPL_Data = yf.Ticker(AAPL)
AMZN_Data = yf.Ticker(Amazon)
GOOGL_Data = yf.Ticker(Google)
#ADA_Data = yf.Ticker(Cardano)
#MATIC_Data = yf.Ticker(Polygon)
#UNI_Data = yf.Ticker(Uniswap)
#DOGE_Data = yf.Ticker(Doge)

period = ["ytd", "max", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y"]
time_period = st.selectbox("Date Range", period)

BTC_His = BTC_Data.history(period=time_period)
ETH_His = ETH_Data.history(period=time_period)
DOT_His = DOT_Data.history(period=time_period)
ATOM_His = ATOM_Data.history(period=time_period)
QNT_His = QNT_Data.history(period=time_period)
HEX_His = HEX_Data.history(period=time_period)
SOL_His = SOL_Data.history(period=time_period)
AVAX_His = AVAX_Data.history(period=time_period)
TSLA_His = TSLA_Data.history(period=time_period)
AAPL_His = AAPL_Data.history(period=time_period)
AMZN_His = AMZN_Data.history(period=time_period)
GOOGL_His = GOOGL_Data.history(period=time_period)
#ADA_His = ADA_Data.history(period=time_period)
#MATIC_His = MATIC_Data.history(period=time_period)
#UNI_His = UNI_Data.history(period=time_period)
#DOGE_His = DOGE_Data.history(period=time_period)

btc, eth, dot, atom = st.columns(4)

with btc:
    st.subheader("BITCOIN")
    imageBTC = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png")
    )
    st.image(imageBTC)
    st.write("Bitcoin Price")
    st.line_chart(BTC_His.Close)
    st.write("Bitcoin Volume")
    st.bar_chart(BTC_His.Volume, width=330, height=230)

with eth:
    st.subheader("Ethereum")
    imageETH = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png")
    )
    st.image(imageETH)
    st.write("Ethereum Price")
    st.line_chart(ETH_His.Close)
    st.write("Ethereum Volume")
    st.bar_chart(ETH_His.Volume, width=330, height=230)

with dot:
    st.subheader("Polkadot")
    imageDOT = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png")
    )
    st.image(imageDOT)
    st.write("Polkadot Price")
    st.line_chart(DOT_His.Close)
    st.write("Polkadot Volume")
    st.bar_chart(DOT_His.Volume, width=330, height=230)

with atom:
    st.subheader("Cosmos")
    imageATOM = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/3794.png")
    )
    st.image(imageATOM)
    st.write("Cosmos Price")
    st.line_chart(ATOM_His.Close)
    st.write("Cosmos Volume")
    st.bar_chart(ATOM_His.Volume, width=330, height=230)

qnt, link, sol, avax = st.columns(4)

with qnt:
    st.subheader("Quant")
    imageQNT = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/3155.png")
    )
    st.image(imageQNT)
    st.write("Quant Price")
    st.line_chart(QNT_His.Close)
    st.write("Quant Volume")
    st.bar_chart(QNT_His.Volume, width=330, height=230)

with link:
    st.subheader("HEX")
    imageLINK = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5015.png")
    )
    st.image(imageLINK)
    st.write("HEX Price")
    st.line_chart(HEX_His.Close)
    st.write("HEX Volume")
    st.bar_chart(HEX_His.Volume, width=330, height=230)

with sol:
    st.subheader("Solana")
    imageSOL = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png")
    )
    st.image(imageSOL)
    st.write("Solana Price")
    st.line_chart(SOL_His.Close)
    st.write("Solana Volume")
    st.bar_chart(SOL_His.Volume, width=330, height=230)

with avax:
    st.subheader("Avalanche")
    imageAVAX = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5805.png")
    )
    st.image(imageAVAX)
    st.write("Avalanche Price")
    st.line_chart(AVAX_His.Close)
    st.write("Avalanche Volume")
    st.bar_chart(AVAX_His.Volume, width=330, height=230)
 
#ada, matic, uni, doge = st.columns(4)
# 
#with ada:
#    st.subheader("Cardano")
#    imageADA = Image.open(
#        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png")
#    )
#    st.image(imageADA)
#    st.write("Cardano Price")
#    st.line_chart(ADA_His.Close)
#    st.write("Cardano Volume")
#    st.bar_chart(ADA_His.Volume, width=330, height=230)
#    
#with matic:
#    st.subheader("Polygon")
#    imageMATIC = Image.open(
#        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png")
#    )
#    st.image(imageMATIC)
#    st.write("Polygon Price")
#    st.line_chart(MATIC_His.Close)
#    st.write("Polygon Volume")
#    st.bar_chart(MATIC_His.Volume, width=330, height=230)
#    
#with uni:
#    st.subheader("Uniswap")
#    imageUNI = Image.open(
#        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/7083.png")
#    )
#    st.image(imageUNI)
#    st.write("Uniswap Price")
#    st.line_chart(UNI_His.Close)
#    st.write("Uniswap Volume")
#    st.bar_chart(UNI_His.Volume, width=330, height=230)
#    
#with doge:
#    st.subheader("Doge Coin")
#    imageDOGE = Image.open(
#        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/74.png")
#    )
#    st.image(imageDOGE)
#    st.write("Doge Coin Price")
#    st.line_chart(DOGE_His.Close)
#    st.write("Doge Coin Volume")
#    st.bar_chart(DOGE_His.Volume, width=330, height=230)

tsla, AAPL, AMZN, GOOGL = st.columns(4)

with tsla:
    st.subheader("Tesla")
    imageTSLA = Image.open(
        urlopen(
            "https://imgs.search.brave.com/-PJXWk0m_116Q2RAi7ztlpUu6db_ShjHQ3f6DRNLmYM/rs:fit:80:80:1/g:ce/aHR0cHM6Ly84bWFy/a2V0Y2FwLmNvbS9p/bWc1L1RTTEEucG5n"
        )
    )
    st.image(imageTSLA)
    st.write("Tesla Price")
    st.line_chart(TSLA_His.Close)
    st.write("Tesla Volume")
    st.bar_chart(TSLA_His.Volume, width=330, height=230)

with AAPL:
    st.subheader("Apple")
    imageAAPL = Image.open(
        urlopen(
            "https://imgs.search.brave.com/LMx9bbR-Y0CnHSKz3gF-mal8vhKoYhXA7kXnJVx8mek/rs:fit:96:96:1/g:ce/aHR0cDovL2ZpbGVz/LnNvZnRpY29ucy5j/b20vZG93bmxvYWQv/c3lzdGVtLWljb25z/L2FwcGxlLWxvZ28t/aWNvbnMtYnktdGh2/Zy9wbmcvOTYvQXBw/bGUlMjBsb2dvJTIw/aWNvbiUyMC0lMjBB/bHVtaW51bS5wbmc"
        )
    )
    st.image(imageAAPL)
    st.write("Apple Price")
    st.line_chart(AAPL_His.Close)
    st.write("Apple Volume")
    st.bar_chart(AAPL_His.Volume, width=330, height=230)


with AMZN:
    st.subheader("Amazon")
    imageAMZN = Image.open(
        urlopen(
            "https://logosmarcas.net/wp-content/uploads/2020/04/Amazon-Simbolo-180x101.png"
        )
    )
    st.image(imageAMZN)
    st.write("Amazon Price")
    st.line_chart(AMZN_His.Close)
    st.write("Amazon Volume")
    st.bar_chart(AMZN_His.Volume, width=330, height=230)

with GOOGL:
    st.subheader("Google (Alphabet Inc)")
    imageGOOGL = Image.open(
        urlopen(
            "https://imgs.search.brave.com/bnPJB9T3tKKADgs8VhlBtG2jIyC7IftGdyo8dfvIgks/rs:fit:140:88:1/g:ce/aHR0cHM6Ly8xMDAw/bG9nb3MubmV0L3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDE2LzEx/L0dvb2dsZS1TeW1i/b2wtMTQweDg4LnBu/Zw"
        )
    )
    st.image(imageGOOGL)
    st.write("Google Price")
    st.line_chart(GOOGL_His.Close)
    st.write("Google Volume")
    st.bar_chart(GOOGL_His.Volume, width=330, height=230)


st.warning("Disclaimer: The tools provided on this website are for informational purposes only and should not be construed as financial advice. Please consult with a licensed financial professional before making any financial decisions. This website is free to use and share.")
