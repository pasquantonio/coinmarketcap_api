#!/usr/bin/env python
"""
This program interacts with the coinmarketcap.com API, makes requests for
ticker information, you give the coin and it returns the info. This is a basic
program but much more could be built from it. However, as far as I can tell
this API is very rudimentary and is not a 'realtime' price.
"""
import requests
import time


class Ticker:
    """
    Consumes the Ticker json object from coinmarketcap and stores
    all its attributes

    -------
    "id"
    "name"
    "symbol"
    "rank"
    "price_usd"
    "price_btc"
    "24h_volume_usd"
    "market_cap_usd"
    "available_supply"
    "total_supply"
    "percent_change_1h"
    "percent_change_24h"
    "percent_change_7d"
    "last_updated"
    -------
    """
    def __init__(self, id, name, symbol, rank, price_usd, price_btc,
                 twentyfourh_volume_usd, market_cap_usd, available_supply,
                 total_supply, percent_change_1h, percent_change_24h,
                 percent_change_7d, last_updated):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.rank = rank
        self.price_usd = price_usd
        self.price_btc = price_btc
        self.twentyfourh_volume_usd = twentyfourh_volume_usd
        self.market_cap_usd = market_cap_usd
        self.available_supply = available_supply
        self.total_supply = total_supply
        self.percent_change_1h = percent_change_1h
        self.percent_change_24h = percent_change_24h
        self.percent_change_7d = percent_change_7d
        self.last_updated = last_updated


class Retriever:
    """
    Requests and retrieves data by hitting the API
    """
    def __init__(self, base, ticker=""):
        """
        if ticker is left blank all currencies are returned
        """
        self.base = base
        self.ticker = ticker
        self.url = self.base + self.ticker

    def _request(self):
        """
        :return: json object of individual ticker
        """
        response = requests.get(self.url)
        return response.json()

    def build_ticker(self):
        """
        GET request to coinmarketcap.com for Ticker info
        :return: Ticker object
        """
        tkr = self._request()
        ticker = Ticker(tkr[0]["id"], tkr[0]["name"], tkr[0]["symbol"],
                        tkr[0]["rank"], tkr[0]["price_usd"],
                        tkr[0]["price_btc"], tkr[0]["24h_volume_usd"],
                        tkr[0]["market_cap_usd"], tkr[0]["available_supply"],
                        tkr[0]["total_supply"], tkr[0]["percent_change_1h"],
                        tkr[0]["percent_change_24h"],
                        tkr[0]["percent_change_7d"], tkr[0]["last_updated"])
        return ticker


if __name__ == "__main__":
    base_url = "https://api.coinmarketcap.com/v1/ticker/"
    ticker = "bitcoin"
    retriever = Retriever(base_url, ticker)
    while True:
        data = retriever.build_ticker()
        print(data.id, data.price_usd)
        time.sleep(10)
