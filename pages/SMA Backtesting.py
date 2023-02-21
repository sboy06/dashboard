import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.graph_objs as go
from PIL import Image
import requests


class CryptoTrader:
    def __init__(self):
        self.crypto = None
        self.data = None
        self.position = None
        self.signal = None

    def set_page_config(self, layout="wide"):
        st.set_page_config(layout=layout)

    def hide_streamlit_style(self):
        hide_streamlit_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    def select_crypto(self):
        self.crypto = st.selectbox(
            "Select a cryptocurrency",
            [
                "BTC-USD",
                "ETH-USD",
                "DOT-USD",
                "ATOM-USD",
                "HEX-USD",
                "QNT-USD",
                "BNB-USD",
                "LINK-USD",
                "XLM-USD",
                "FET-USD",
                "EWT-USD",
                "SAITAMA-USD",
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
            ],
        )

    def get_data(self):
        self.data = yf.Ticker(self.crypto).history(period="6mo")
        self.data["8_SMA"] = self.data["Close"].rolling(window=8).mean()
        self.data["20_SMA"] = self.data["Close"].rolling(window=20).mean()

    def backtesting(self):
        self.data["position"] = None
        self.data["Signal"] = None
        for i in range(len(self.data)):
            if (self.data["8_SMA"].iloc[i] > self.data["20_SMA"].iloc[i]) and (
                self.data["8_SMA"].iloc[i - 1] <= self.data["20_SMA"].iloc[i - 1]
            ):
                self.data["position"].iloc[i] = 1
                self.data["Signal"].iloc[i] = "Buy"
            elif (self.data["8_SMA"].iloc[i] < self.data["20_SMA"].iloc[i]) and (
                self.data["8_SMA"].iloc[i - 1] >= self.data["20_SMA"].iloc[i - 1]
            ):
                self.data["position"].iloc[i] = -1
                self.data["Signal"].iloc[i] = "Sell"

    def create_chart(self):
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=self.data.index, y=self.data["Close"], name="Close Price")
        )
        fig.add_trace(go.Scatter(x=self.data.index, y=self.data["8_SMA"], name="8 SMA"))
        fig.add_trace(
            go.Scatter(x=self.data.index, y=self.data["20_SMA"], name="20 SMA")
        )
        fig.add_trace(
            go.Scatter(
                x=self.data[self.data["Signal"] == "Buy"].index,
                y=self.data.loc[self.data["Signal"] == "Buy", "Close"],
                mode="markers",
                name="Buy",
                marker=dict(size=10, color="green", symbol="circle"),
                text=self.data[self.data["Signal"] == "Buy"].index,
            )
        )
        fig.add_trace(
            go.Scatter(
                x=self.data[self.data["Signal"] == "Sell"].index,
                y=self.data.loc[self.data["Signal"] == "Sell", "Close"],
                mode="markers",
                name="Sell",
                marker=dict(size=10, color="red", symbol="cross"),
                text=self.data[self.data["Signal"] == "Sell"].index,
            )
        )
        fig.update_layout(
            title="Backtesting of 8 and 20 SMA for " + self.crypto,
            xaxis_title="Date",
            yaxis_title="Price",
            yaxis_type="log",
            xaxis=dict(showgrid=True, title_font=dict(size=14), tickfont=dict(size=12)),
            yaxis=dict(showgrid=True, title_font=dict(size=14), tickfont=dict(size=12)),
        )
        st.plotly_chart(fig, use_container_width=True, height=600)


if __name__ == "__main__":
    cryptotrader = CryptoTrader()
    cryptotrader.set_page_config()
    cryptotrader.hide_streamlit_style()
    cryptotrader.select_crypto()
    cryptotrader.get_data()
    cryptotrader.backtesting()
    cryptotrader.create_chart()
