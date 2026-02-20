import yfinance as yf
from typing import List, Dict
from app.pipeline.collectors.base_collector import BaseCollector


class YFinanceCollector(BaseCollector):
    """
    Coletor de dados financeiros via yFinance.
    """

    def __init__(self, symbol: str):
        self.symbol = symbol

    def collect(self) -> List[Dict]:
        ticker = yf.Ticker(self.symbol)
        data = ticker.history(period="1d")

        if data.empty:
            return []

        latest = data.iloc[-1]

        return [
            {
                "description": f"{self.symbol} price",
                "amount": float(latest["Close"]),
            }
        ]
