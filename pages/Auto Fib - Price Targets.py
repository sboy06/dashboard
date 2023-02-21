import yfinance as yf
import streamlit as st
import plotly.graph_objects as go
import numpy as np



class CryptoPriceTargets:
    st.set_page_config(
        page_title="Crypto Currency Price Targets",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )
    
    imageLOGO = Image.open(urlopen("https://i.ibb.co/mhwTKWs/sboy-logo.png"))
    st.image(imageLOGO)
    
    def __init__(self):
        self.ticker = st.selectbox(
            "Select a Crypto Currency:",
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

    @st.cache
    def get_data(self):
        return yf.download(self.ticker, period="10mo")

    def plot_chart(self):
        data = self.get_data()

        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=data.index,
                    open=data["Open"],
                    high=data["High"],
                    low=data["Low"],
                    close=data["Close"],
                )
            ]
        )

        # Get the peak and trough of the prices
        peak = data["High"].max()
        trough = data["Low"].min()

        fig.add_shape(
            # Line Horizontal
            type="line",
            x0=data.index[0],
            y0=trough,
            x1=data.index[-1],
            y1=trough,
            line=dict(color="gray", width=1, dash="dot"),
        )
        fig.add_shape(
            # Line Horizontal
            type="line",
            x0=data.index[0],
            y0=peak,
            x1=data.index[-1],
            y1=peak,
            line=dict(color="gray", width=1, dash="dot"),
        )

        # Calculate the Fibonacci retracement levels
        fib_382 = peak - (peak - trough) * 0.382
        fib_50 = peak - (peak - trough) * 0.5
        fib_618 = peak - (peak - trough) * 0.618

        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=np.array([fib_382] * len(data.index)),
                mode="lines",
                name="Fibonacci 38.2%",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=np.array([fib_50] * len(data.index)),
                mode="lines",
                name="Fibonacci 50%",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=np.array([fib_618] * len(data.index)),
                mode="lines",
                name="Fibonacci 61.8%",
            )
        )

        fig.update_layout(
            title=f"{self.ticker} Candlestick Chart with Fibonacci Retracement",
            xaxis_title="Date",
            yaxis_title="Price",
        )

        fig.add_trace(
            go.Candlestick(
                x=data.index,
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"],
                increasing=dict(line=dict(color="green")),
                decreasing=dict(line=dict(color="red")),
            )
        )

        fig.update_layout(legend=dict(x=0, y=1, traceorder="normal"))

        fig.update_layout(template="plotly_white", margin=dict(r=10, t=25, b=40, l=60))

        st.plotly_chart(fig, use_container_width=True, height=600)

        st.write("Price Targets:")
        st.write("38.2% Fibonacci: ", fib_382)
        st.write("50% Fibonacci: ", fib_50)
        st.write("61.8% Fibonacci: ", fib_618)


if __name__ == "__main__":
    crypto_prices = CryptoPriceTargets()
    crypto_prices.plot_chart()


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
