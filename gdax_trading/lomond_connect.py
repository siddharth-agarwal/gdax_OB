from lomond.websocket import WebSocket
import json
import requests

gdax_http_endpoint='https://api.gdax.com'
gdax_ws_endpoint='wss://ws-feed.gdax.com'

subscribe_msg={"type": "subscribe","product_ids": ["LTC-USD"]}

# ob_request='/products/BTC-USD/book?level=3'

def getProductOrderBook (self, json=None, level=3, product=''):
  r = requests.get(self.url + '/products/%s/book?level=%s' % (product, str(level)))
  return r.json()

ws = WebSocket(gdax_ws_endpoint)
for event in ws.connect():
    # print(event)
    if event.name == 'poll':
      ws.send_text(json.dumps(subscribe_msg))
    elif event.name == 'text':
      print(event.text)