import requests

gdax_http_endpoint='https://api.gdax.com'

class HTTPClient:
  def __init__ (self, product):
    self.product = product

  def getProducts(self):
    r = requests.get(gdax_http_endpoint + '/products')
    return r.json()

  def getProductOrderBook (self, level):
    r = requests.get(gdax_http_endpoint + '/products/%s/book?level=%s' % (self.product, str(level)))
    return r.json()

  def getProductTrades (self):
    r = requests.get(gdax_http_endpoint + '/products/%s/trades' % (self.product))
    return r.json()

    # def getProductHistoricRates(self, product, start, end, granularity):
    #   payload = {}
    #   payload["start"] = start
    #   payload["end"] = end
    #   payload["granularity"] = granularity
    #   r = requests.get(self.url + '/products/%s/candles' % (product or self.productId), params=payload)
    #   return r.json()
    #
    # def getProduct24HrStats(self, json=None, product=''):
    #   r = requests.get(self.url + '/products/%s/stats' % (product or self.productId))
    #   return r.json()
    #
    # def getCurrencies(self):
    #   r = requests.get(self.url + '/currencies')
    #   return r.json()
    #
    # def getTime(self):
    #   r = requests.get(self.url + '/time')
    #   return r.json()
