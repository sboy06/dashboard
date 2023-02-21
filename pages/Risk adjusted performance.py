import contextlib
import warnings
import yfinance as yf
import pandas as pd
import riskfolio as rp
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
import datetime


class RiskAdjustedPerformance:
    def __init__(self):
        st.set_page_config(layout="wide")

        self.hide_streamlit_style = """
                    <style>
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(self.hide_streamlit_style, unsafe_allow_html=True)
        imageLOGO = Image.open(urlopen("https://i.ibb.co/mhwTKWs/sboy-logo.png"))
        st.image(imageLOGO)
        st.title("Risk adjusted performance")
        st.markdown("")
        st.warning(
            "Select multiple assets to compare their risk-adjusted performance in order to determine the optimal portfolio."
        )
        st.markdown("---")

        self.all_assets = [
            "BTC-USD",
            "ETH-USD",
            "DOT-USD",
            "AVAX-USD",
            "ATOM-USD",
            "HEX-USD",
            "FET-USD",
            "EWT-USD",
            "SAITAMA-USD",
            "QNT-USD",
            "BNB-USD",
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
        ]

    def download_data(self):
        warnings.filterwarnings("ignore")

        pd.options.display.float_format = "(:.4%}".format

        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=365 * 3)

        assets = st.multiselect(
            "Select assets to include in portfolio:", self.all_assets
        )

        with contextlib.suppress(ValueError, TypeError):
            self._extracted_from_download_data_(assets, start, end)

    # TODO Rename this here and in `download_data`
    def _extracted_from_download_data_(self, assets, start, end):
        # Download data and select 'Adj Close' columns
        data = yf.download(assets, start=start, end=end)
        data = data.loc[:, ("Adj Close", slice(None))]

        data.columns = assets

        tickers = data.pct_change().dropna()

        Y = tickers

        method_mu = "hist"
        method_cov = "hist"
        hist = True
        model = "Classic"
        rm = "MV"
        obj = "Sharpe"
        rf = 0
        l = 0

        port = rp.Portfolio(returns=Y)
        port.assets_stats(method_mu=method_mu, method_cov=method_cov)

        w = port.optimization(model=model, rm=rm, obj=obj, rf=rf, l=l, hist=hist)

        ws = port.efficient_frontier(
            model="Classic", rm=rm, points=20, rf=rf, hist=hist
        )

        w2 = port.rp_optimization(model="Classic", rm=rm, rf=rf, b=None, hist=hist)

        sns.set_style("whitegrid")

        fig, ax = plt.subplots(figsize=(6, 4))

        ax.pie(
            w.values.flatten(),
            labels=w.index,
            autopct="%1.1f%%",
            startangle=90,
            textprops={"fontsize": 14, "color": "black"},
        )

        plt.title("Optimized Portfolio", fontsize=18)
        plt.legend(title="Assets")

        plt.savefig("optimized_portfolio.png")
        st.image("optimized_portfolio.png", caption="Optimized Portfolio", width=600)


if __name__ == "__main__":
    riskadjustedperformance = RiskAdjustedPerformance()
    riskadjustedperformance.download_data()
