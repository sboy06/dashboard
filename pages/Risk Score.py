import streamlit as st
import plotly.graph_objects as go
import yfinance as yf
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen
from PIL import Image
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class CryptoRiskAnalysis:
    def __init__(self):
        st.set_page_config(layout="wide")

        hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    def run(self):
        imageLOGO = Image.open(urlopen("https://i.ibb.co/mhwTKWs/sboy-logo.png"))
        st.image(imageLOGO)
        st.title("Cryptocurrency Risk Analysis")

        ticker = st.selectbox(
            "Select the ticker of the cryptocurrency or Stock you want to analyze: ",
            [
                "BTC-USD",
                "ETH-USD",
                "DOT-USD",
                "ATOM-USD",
                "HEX-USD",
                "QNT-USD",
                "BNB-USD",
                "LINK-USD",
                "FET-USD",
                "EWT-USD",
                "SAITAMA-USD",
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
            ],
        )

        current_date = datetime.now().date()

        # Get historical data for the ticker
        data = yf.download(ticker, start="2021-11-01", end=current_date)

        # Calculate risk score (this is an example, the risk score calculation should be tailored to your needs)
        risk_score = (data["Close"].max() - data["Close"].iloc[-1]) / data[
            "Close"
        ].mean()

        # Create the plotly figure
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Close")
        )

        # Add heat color
        if risk_score < 1:
            color = "#0099ff"
        elif risk_score < 2.5:
            color = "#00ff99"
        elif risk_score < 5:
            color = "#ffff00"
        else:
            color = "#ff3333"
        fig.update_layout(
            title=f"{ticker} Risk Score: {risk_score:.2f}",
            title_x=0.5,
            shapes=[
                dict(
                    type="line",
                    x0=data.index[0],
                    y0=data["Close"].iloc[-1],
                    x1=data.index[-1],
                    y1=data["Close"].iloc[-1],
                    line=dict(color=color, width=2),
                )
            ],
        )
        st.warning(
            "A risk score is a numerical value that is used to assess the level of risk associated with a particular individual, event, or activity. It is a tool used to quantify and measure the likelihood of an adverse event occurring. The score is calculated using a set of predetermined criteria and factors such as credit history, financial stability, or past behavior. High Risk = High Reward"
        )
        st.plotly_chart(fig, use_container_width=True, height=600)

        st.markdown(
            """
            <style>
            .risk-legend {
                display: flex;
                justify-content: space-between;
            }
            .risk-legend .risk-level {
                width: 20px;
                height: 20px;
                margin-right: 10px;
            }
            </style>
            <div class="risk-legend">
                <div style='display: flex;align-items: center;'>
                    <div class="risk-level" style="background-color: #0099ff"></div>
                    <div style='padding-left:10px'>Low Risk</div>
                </div>
                <div style='display: flex;align-items: center;'>
                    <div class="risk-level" style="background-color: #00ff99"></div>
                    <div style='padding-left:10px'>Medium Risk</div>
                </div>
                <div style='display: flex;align-items: center;'>
                    <div class="risk-level" style="background-color: #ffff00"></div>
                    <div style='padding-left:10px'>High Risk</div>
                </div>
                <div style='display: flex;align-items: center;'>
                    <div class="risk-level" style="background-color: #ff3333"></div>
                    <div style='padding-left:10px'>Very High Risk</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("")
        st.markdown("")
        st.markdown("---")


if __name__ == "__main__":
    app = CryptoRiskAnalysis()
    app.run()
