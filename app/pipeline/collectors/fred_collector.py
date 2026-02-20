import os
from typing import List, Dict
from fredapi import Fred
from app.pipeline.collectors.base_collector import BaseCollector


class FREDCollector(BaseCollector):
    """
    Coletor de indicadores macroeconômicos via FRED.
    """

    def __init__(self, series_id: str):
        self.series_id = series_id
        self.api_key = os.getenv("FRED_API_KEY")

        if not self.api_key:
            raise ValueError("FRED_API_KEY not configured")

        self.fred = Fred(api_key=self.api_key)

    def collect(self) -> List[Dict]:
        data = self.fred.get_series(self.series_id)

        if data.empty:
            return []

        latest_value = data.iloc[-1]

        return [
            {
                "description": f"FRED {self.series_id}",
                "amount": float(latest_value),
            }
        ]