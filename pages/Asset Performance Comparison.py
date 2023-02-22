import streamlit as st
import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


class CryptocurrencyPerformance:
    def __init__(self):
        st.set_page_config(layout="wide")
        hide_streamlit_style = """
                    <style>
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
        self.tickers = (
            "BTC-USD",
            "ETH-USD",
            "DOT-USD",
            "ATOM-USD",
            "HEX-USD",
            "QNT-USD",
            "BNB-USD",
            "FET-USD",
            "EWT-USD",
            "SAITAMA-USD",
            "LINK-USD",
            "XLM-USD",
            "CRO-USD",
            "HBAR-USD",
            "ADA-USD",
            "GLMR-USD",
            "ASTR-USD",
            "ALGO-USD",
            "DYDX-USD",
            "NEAR-USD",
            "MATIC-USD",
            "SHIB-USD",
            "DOGE-USD",
            "LTC-USD",
            "XTZ-USD",
            "THETA-USD",
            "BTT-USD",
            "FTM-USD",
            "OSMO-USD",
            "HNT-USD",
            "YFI-USD",
            "KDA-USD",
            "SUSHI-USD",
            "XRP-USD",
            "SOL-USD",
            "UNI7083-USD",
            "XMR-USD",
            "VET-USD",
            "FIL-USD",
            "LUNC-USD",
            "ICP-USD",
            "EOS-USD",
            "SAND-USD",
            "APE18876-USD",
            "AAVE-USD",
            "ZEC-USD",
            "GRT6719-USD",
            "1INCH-USD",
            "RSR-USD",
            "CSPR-USD",
            "KAVA-USD",
            "RVN-USD",
            "KSM-USD",
            "ACA-USD",
            "GODS-USD",
            "TSLA",
            "NIO",
            "RIVN",
            "AAPL",
            "NVDA",
            "MSFT",
            "META",
            "GOOGL",
            "NFLX",
            "SNAP",
            "AMD",
            "AMC",
            "AMZN",
            "BABA",
            "UBER",
            "LYFT",
            "SHOP",
            "COIN",
            "RBLX",
            "CSCO",
            "NKE",
            "BA",
            "V",
            "WMT",
            "TMUS",
            "ZM",
            "T",
            "INTC",
            "TLRY",
            "HOOD",
            "SWN",
            "C",
            "CGC",
            "AAL",
            "DIS",
            "PFE",
            "XOM",
            "PYPL",
            "KO",
            "PINS",
            "HPE",
            "X",
            "WBA",
            "PRI",
            "ROKU",
            "MRVL",
            "QCOM",
            "DAL",
            "CVX",
            "SBUX",
            "LUV",
            "WU",
            "GE",
            "DASH",
            "PEP",
            "EBAY",
            "ABNB",
            "BRK-B",
            "WYNN",
            "TGT",
            "SHEL",
            "MGM",
            "VTSAX",
            "SPX",
        )

    def app(self):
        st.title("Cryptocurrency & Stock Performance")
        st.write("Performance Application")

    def display_as_percentage(self):
        return "{:.1f}%".format(self * 100)

    def run(self):
        dropdown = st.multiselect("Pick your assets", self.tickers)
        start = st.date_input("Start Date", value=pd.to_datetime("2021-01-01"))
        end = st.date_input("End Date", value=pd.to_datetime("today"))

        def relativeret(df):
            rel = df.pct_change()
            cumret = (1 + rel).cumprod() - 1
            cumret = cumret.fillna(0)
            return cumret

        if len(dropdown) > 0:
            df = relativeret(yf.download(dropdown, start, end)["Adj Close"])
            st.header("Returns of {}".format(dropdown))
            st.line_chart(df)


if __name__ == "__main__":
    cp = CryptocurrencyPerformance()
    cp.app()
    cp.run()
