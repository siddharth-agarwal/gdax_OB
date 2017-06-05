import requests

gdax_http_endpoint='https://api.gdax.com'

class HTTPClient:

  def __init__(self, products):
    self.url=gdax_http_endpoint
    self.productId = products

  def getProducts(self):
    r = requests.get(self.url + '/products')
    return r.json()

  def getProductOrderBook(self, level, product):
    r = requests.get(self.url + '/products/%s/book?level=%s' % (product or self.productId, str(level)))
    return r.json()

  def getProductTicker(self, product):
    r = requests.get(self.url + '/products/%s/ticker' % (product or self.productId))
    return r.json()

  def getProductTrades(self, product):
    r = requests.get(self.url + '/products/%s/trades' % (product or self.productId))
    return r.json()

  def getProductHistoricRates(self, product, start, end, granularity):
    payload = {}
    payload["start"] = start
    payload["end"] = end
    payload["granularity"] = granularity
    r = requests.get(self.url + '/products/%s/candles' % (product or self.productId), params=payload)
    return r.json()

  def getProduct24HrStats(self, json=None, product=''):
    r = requests.get(self.url + '/products/%s/stats' % (product or self.productId))
    return r.json()

  def getCurrencies(self):
    r = requests.get(self.url + '/currencies')
    return r.json()

  def getTime(self):
    r = requests.get(self.url + '/time')
    return r.json()