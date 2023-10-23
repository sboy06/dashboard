import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen
from datetime import datetime
from streamlit_extras.app_logo import add_logo
import ssl
 
ssl._create_default_https_context = ssl._create_unverified_context

current_dateTime = datetime.now()

st.set_page_config(
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)
add_logo("https://i.ibb.co/GCtVYbv/sboylogo-no-Bg.png", height=300)

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
st.markdown(
    "<h2 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 17px; border: 2px solid white; display: inline-block; margin: 30px 20px 20px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Volume & Price Charts</h2>",
    unsafe_allow_html=True,
)

st.sidebar.success("Select which tool you want to use")

HEX = "HEX-USD"
Pulsechain = "PLS-USD"
Bitcoin = "BTC-USD"
Ethereum = "ETH-USD"
Polkadot = "DOT-USD"
Cosmos = "ATOM-USD"
Quant = "QNT-USD"
Aptos = "APT21794-USD"
Solana = "SOL-USD"
Avalanche = "AVAX-USD"
Tesla = "TSLA"
AAPL = "AAPL"
Amazon = "AMZN"
Google = "GOOGL"

HEX_Data = yf.Ticker(HEX)
PLS_Data = yf.Ticker(Pulsechain)
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
DOT_Data = yf.Ticker(Polkadot)
ATOM_Data = yf.Ticker(Cosmos)
QNT_Data = yf.Ticker(Quant)
Aptos_Data = yf.Ticker(Aptos)
SOL_Data = yf.Ticker(Solana)
AVAX_Data = yf.Ticker(Avalanche)
TSLA_Data = yf.Ticker(Tesla)
AAPL_Data = yf.Ticker(AAPL)
AMZN_Data = yf.Ticker(Amazon)
GOOGL_Data = yf.Ticker(Google)

period = ["ytd", "max", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y"]
time_period = st.selectbox("Date Range", period)

PLS_His = PLS_Data.history(period=time_period)
HEX_His = HEX_Data.history(period=time_period)
BTC_His = BTC_Data.history(period=time_period)
ETH_His = ETH_Data.history(period=time_period)
DOT_His = DOT_Data.history(period=time_period)
ATOM_His = ATOM_Data.history(period=time_period)
QNT_His = QNT_Data.history(period=time_period)
Aptos_His = Aptos_Data.history(period=time_period)
SOL_His = SOL_Data.history(period=time_period)
AVAX_His = AVAX_Data.history(period=time_period)
TSLA_His = TSLA_Data.history(period=time_period)
AAPL_His = AAPL_Data.history(period=time_period)
AMZN_His = AMZN_Data.history(period=time_period)
GOOGL_His = GOOGL_Data.history(period=time_period)


hex, pls = st.columns(2)

with hex:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>eHEX</h5>",
        unsafe_allow_html=True,
    )
    imageHEX = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5015.png")
    )
    st.image(imageHEX)
    st.write("HEX Price")
    st.line_chart(HEX_His.Close)
    st.write("HEX Volume")
    st.bar_chart(HEX_His.Volume, width=330, height=230)

with pls:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>PulseChain</h5>",
        unsafe_allow_html=True,
    )
    imagePLS = Image.open(urlopen("https://pulsechain.com/img/wordmark.png"))

    new_dimensions = (200, 200)

    image_resized = imagePLS.resize(new_dimensions, Image.ANTIALIAS)
 
    st.image(imagePLS)
    st.write("PLS Price")
    st.line_chart(PLS_His.Close)
    st.write("HEX Volume")
    st.bar_chart(PLS_His.Volume, width=330, height=230)

btc, eth, dot, atom = st.columns(4)

with btc:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Bitcoin</h5>",
        unsafe_allow_html=True,
    )
    imageBTC = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png")
    )
    st.image(imageBTC)
    st.write("Bitcoin Price")
    st.line_chart(BTC_His.Close)
    st.write("Bitcoin Volume")
    st.bar_chart(BTC_His.Volume, width=330, height=230)

with eth:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Ethereum</h5>",
        unsafe_allow_html=True,
    )
    imageETH = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png")
    )
    st.image(imageETH)
    st.write("Ethereum Price")
    st.line_chart(ETH_His.Close)
    st.write("Ethereum Volume")
    st.bar_chart(ETH_His.Volume, width=330, height=230)

with dot:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Polkadot</h5>",
        unsafe_allow_html=True,
    )
    imageDOT = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png")
    )
    st.image(imageDOT)
    st.write("Polkadot Price")
    st.line_chart(DOT_His.Close)
    st.write("Polkadot Volume")
    st.bar_chart(DOT_His.Volume, width=330, height=230)

with atom:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Cosmos</h5>",
        unsafe_allow_html=True,
    )
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
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Quant</h5>",
        unsafe_allow_html=True,
    )
    imageQNT = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/3155.png")
    )
    st.image(imageQNT)
    st.write("Quant Price")
    st.line_chart(QNT_His.Close)
    st.write("Quant Volume")
    st.bar_chart(QNT_His.Volume, width=330, height=230)

with link:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Aptos</h5>",
        unsafe_allow_html=True,
    )
    imageLINK = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/21794.png")
    )
    st.image(imageLINK)
    st.write("Aptos Price")
    st.line_chart(Aptos_His.Close)
    st.write("Aptos Volume")
    st.bar_chart(Aptos_His.Volume, width=330, height=230)

with sol:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Solana</h5>",
        unsafe_allow_html=True,
    )
    imageSOL = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png")
    )
    st.image(imageSOL)
    st.write("Solana Price")
    st.line_chart(SOL_His.Close)
    st.write("Solana Volume")
    st.bar_chart(SOL_His.Volume, width=330, height=230)

with avax:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Avalanche</h5>",
        unsafe_allow_html=True,
    )
    imageAVAX = Image.open(
        urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5805.png")
    )
    st.image(imageAVAX)
    st.write("Avalanche Price")
    st.line_chart(AVAX_His.Close)
    st.write("Avalanche Volume")
    st.bar_chart(AVAX_His.Volume, width=330, height=230)

tsla, AAPL, AMZN, GOOGL = st.columns(4)

with tsla:
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Tesla</h5>",
        unsafe_allow_html=True,
    )
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
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Apple</h5>",
        unsafe_allow_html=True,
    )
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
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Amazon</h5>",
        unsafe_allow_html=True,
    )
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
    st.markdown(
        "<h5 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 5px; border: 2px solid white; display: inline-block; margin: 30px 20px 40px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Google</h5>",
        unsafe_allow_html=True,
    )
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


st.warning(
    "Disclaimer: The tools provided on this website are for informational purposes only and should not be construed as financial advice. Please consult with a licensed financial professional before making any financial decisions. This website is free to use and share."
)
