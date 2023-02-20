import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime


class CryptoData:
    def __init__(self):
        self.st = st
        self.st.set_page_config(layout="wide")
        self.hide_streamlit_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
        self.st.markdown(self.hide_streamlit_style, unsafe_allow_html=True)
        self.st.title("Cryptocurrency Historical Data")
        self.tickers = [
            "BTC-USD",
            "ETH-USD",
            "DOT-USD",
            "ATOM-USD",
            "HEX-USD",
            "QNT-USD",
            "BNB-USD",
            "LINK-USD",
            "XLM-USD",
            "CRO-USD",
            "HBAR-USD",
            "FET-USD",
            "EWT-USD",
            "SAITAMA-USD",
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
        ]
        self.current_date = datetime.now().date()

    def download_data(self):
        self.selected_ticker = self.st.selectbox("Select Ticker", self.tickers)
        try:
            data = yf.download(
                self.selected_ticker, start="2020-01-01", end=self.current_date
            )["Close"]
            self.create_line_chart(data)
        except Exception as e:
            self.st.error("Data not available for the selected ticker.")

    def create_line_chart(self, data):
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=data.index, y=data, name=data.name, line=dict(width=2, color="blue")
            )
        )
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Price",
            title=f"{self.selected_ticker} Historical Data",
            yaxis_type="log",
        )
        x = data.index.to_julian_date().values.reshape(-1, 1)
        y = data.values
        y_log = np.log(y)
        clf = LinearRegression()
        clf.fit(x, y_log)
        y_pred = np.exp(clf.predict(x))
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=y_pred,
                name="Logarithmic Regression",
                line=dict(width=2, color="red", dash="dot"),
            )
        )
        self.st.plotly_chart(fig, use_container_width=True)


crypto_data = CryptoData()
crypto_data.download_data()
