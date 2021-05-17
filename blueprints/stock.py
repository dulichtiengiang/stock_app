from flask import Blueprint, render_template
import requests

stock = Blueprint('stock',__name__, url_prefix='/stock')

#https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL?apikey=demo

API_URL = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{ticker}'

def fetch_price(ticker):
    data=requests.get(API_URL.format(ticker=ticker.upper()), params={'apikey': 'demo'}).json()
    return data['price']

def fetch_income(ticker):
    # https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL?apikey=demo&period=quarter
    url = 'https://financialmodelingprep.com/api/v3/financials/income-statement/{}'.format(ticker)
    financials =requests.get(url, params={'period': 'quarter', 'apikey': 'demo'}).json()['financials']
    financials.sort(key=lambda quarter: quarter["date"])
    return financials

@stock.route('/<ticker>')
def quote(ticker):
    price = fetch_price(ticker)
    return render_template('stock/quote.html',ticker=ticker, ticker_price=price)

@stock.route('/<string:ticker>/financials')
def financials(ticker):
    data= fetch_income(ticker)
    return render_template('stock/financials.html', ticker=ticker, financials=data)