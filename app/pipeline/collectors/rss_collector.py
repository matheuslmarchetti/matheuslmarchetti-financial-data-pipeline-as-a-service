from typing import List, Dict
import feedparser
from app.pipeline.collectors.base_collector import BaseCollector


class RSSCollector(BaseCollector):
    """
    Coletor de notícias financeiras via RSS.
    """

    def __init__(self, feed_url: str):
        self.feed_url = feed_url

    def collect(self) -> List[Dict]:
        feed = feedparser.parse(self.feed_url)

        if not feed.entries:
            return []

        results = []

        for entry in feed.entries[:5]:  # limita a 5 notícias
            results.append(
                {
                    "description": entry.title,
                    "amount": 0.0,  # notícia não tem valor numérico
                }
            )

        return results