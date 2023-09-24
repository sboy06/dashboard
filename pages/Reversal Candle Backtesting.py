import yfinance as yf
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from datetime import datetime, timedelta
from streamlit_extras.app_logo import add_logo

class ReversalCandleDetection:
    def __init__(self):
        st.set_page_config(layout="wide")
        add_logo("https://i.ibb.co/GCtVYbv/sboylogo-no-Bg.png", height=300)

        st.markdown(
            "<h2 style='text-align: center; font-family: Avant Garde; align: center; padding: 5px 17px; border: 2px solid white; display: inline-block; margin: 30px 20px 20px -10px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);'>Reverse Candle Detection App</h2>",
            unsafe_allow_html=True,
        )
        st.warning(
            "This app uses daily candles to identify reversal patterns. If the patterns appear at the top of the trend, it indicates a bearish signal. Conversely, patterns at the bottom of the trend indicate a bullish signal."
        )
        st.markdown("---")

        self.ticker_list = [
            "BTC-USD",
            "ETH-USD",
            "DOT-USD",
            "PLS-USD",
            "APT21794-USD",
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
        self.ticker = st.selectbox("Select a ticker:", self.ticker_list)

        self.end_date = datetime.now()
        self.start_date = self.end_date - timedelta(days=90)

        self.data = yf.download(
            self.ticker, start=self.start_date, end=self.end_date, interval="1d"
        )

        self.fig = make_subplots(rows=1, cols=1)

    def create_candlestick_chart(self):
        self.fig.add_trace(
            go.Candlestick(
                x=self.data.index,
                open=self.data["Open"],
                high=self.data["High"],
                low=self.data["Low"],
                close=self.data["Close"],
                increasing=dict(line=dict(color="#00ff00")),
                decreasing=dict(line=dict(color="#ff0000")),
            )
        )

    def detect_morning_star_candles(self):
        self.morning_star_candles = [
            i
            for i in range(2, len(self.data))
            if (self.data["Close"][i - 2] > self.data["Open"][i - 2])
            and (self.data["Close"][i - 1] < self.data["Open"][i - 1])
            and (self.data["Close"][i] > self.data["Open"][i])
            and (self.data["Open"][i - 1] > self.data["Close"][i - 2])
            and (self.data["Close"][i] > self.data["Open"][i - 1])
        ]
        self.fig.add_trace(
            go.Scatter(
                x=self.data.index[self.morning_star_candles],
                y=self.data["Close"][self.morning_star_candles],
                mode="markers",
                marker=dict(color="orange", size=10),
                name="Evening/Morning Star",
            )
        )

    def detect_bullish_engulfing_candles(self):
        self.bullish_engulfing_candles = [
            i
            for i in range(1, len(self.data))
            if (self.data["Close"][i - 1] < self.data["Open"][i - 1])
            and (self.data["Close"][i] > self.data["Open"][i])
            and (self.data["Open"][i] < self.data["Close"][i - 1])
            and (self.data["Close"][i] > self.data["High"][i - 1])
        ]
        self.fig.add_trace(
            go.Scatter(
                x=self.data.index[self.bullish_engulfing_candles],
                y=self.data["Close"][self.bullish_engulfing_candles],
                mode="markers",
                marker=dict(color="blue", size=10),
                name="Engulfing",
            )
        )

    def detect_hammer_candles(self):
        self.hammer_candles = [
            i
            for i in range(len(self.data))
            if (self.data["Close"][i] > self.data["Open"][i])
            and (self.data["Close"][i] - self.data["Open"][i])
            < (self.data["High"][i] - self.data["Close"][i])
            and (self.data["Close"][i] - self.data["Open"][i])
            > (self.data["Low"][i] - self.data["Open"][i])
        ]
        self.fig.add_trace(
            go.Scatter(
                x=self.data.index[self.hammer_candles],
                y=self.data["Close"][self.hammer_candles],
                mode="markers",
                marker=dict(color="purple", size=10),
                name="Hammer",
            )
        )

    def inverse_hs_candlee(self):
        self.inverse_hs_candles = [
            i
            for i in range(2, len(self.data))
            if (self.data["Low"][i - 2] > self.data["Low"][i - 1])
            and (self.data["Low"][i - 1] > self.data["Low"][i])
            and (self.data["Close"][i - 2] < self.data["Close"][i - 1])
            and (self.data["Close"][i - 1] > self.data["Close"][i])
            and (self.data["Close"][i - 2] < self.data["Close"][i])
        ]
        self.fig.add_trace(
            go.Scatter(
                x=self.data.index[self.inverse_hs_candles],
                y=self.data["Close"][self.inverse_hs_candles],
                mode="markers",
                marker=dict(color="white", size=10),
                name="Inverse Head and Shoulders",
            )
        )

    def update_layout(self):
        self.fig.update_layout(
            xaxis=dict(
                showgrid=True,
                gridcolor="lightgray",
                gridwidth=1,
                showline=True,
                linewidth=1,
                linecolor="lightgray",
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor="lightgray",
                gridwidth=1,
                showline=True,
                linewidth=1,
                linecolor="lightgray",
            ),
        )


if __name__ == "__main__":
    reversal_candle_detection = ReversalCandleDetection()
    reversal_candle_detection.create_candlestick_chart()
    reversal_candle_detection.detect_morning_star_candles()
    reversal_candle_detection.detect_bullish_engulfing_candles()
    reversal_candle_detection.detect_hammer_candles()
    reversal_candle_detection.inverse_hs_candlee()
    reversal_candle_detection.update_layout()
    st.plotly_chart(reversal_candle_detection.fig, use_container_width=True, height=600)


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
