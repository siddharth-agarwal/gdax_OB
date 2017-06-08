import json
from decimal import Decimal

from lomond.websocket import WebSocket

from gdax_trading.HTTPClient import HTTPClient

## refer to GDAX API for details
gdax_ws_endpoint='wss://ws-feed.gdax.com'


## COPIED FROM GDAX API REF
# An algorithm to maintain an up-to-date order book is described below:
# 1. Send a subscribe message for the product of interest.
# 2. Queue any messages received over the websocket stream.
# 3. Make a REST request for the order book snapshot from the REST feed.
# 4. Playback queued messages, discarding sequence numbers before or equal to the snapshot sequence number.
# 5. Apply playback messages to the snapshot as needed (see below).
# 6. After playback is complete, apply real-time stream messages as they arrive.

class OrderBook:
  initial_ob = None

  def __init__ (self, product):
    self.initial_ob = HTTPClient(product=product).getProductOrderBook(level=3)
    self.products = product
    self._sequence = -1
    ## TODO BID/ASK ARRAYS

  def processOBMessage (self, message):
    sequence = message['sequence']
    ## TODO LOGIC

  def add (self, order):
    order = {
      'id': order['order_id'] if 'order_id' in order else order['id'],
      'side': order['side'],
      'price': Decimal(order['price']),
      'size': Decimal(order.get('size', order['remaining_size']))
    }

    # def remove (self, order):
    ## TODO
    # def match (self, order):
    ## TODO
    # def change (self, order):
    ## TODO

  def start(self):
    sub_params = {'type': 'subscribe', 'product_ids': self.products}
    ws = WebSocket(gdax_ws_endpoint)

    for event in ws.connect():
      if event.name == 'poll':
        ws.send_text(json.dumps(sub_params))
      elif event.name == 'text':
        try:
          msg = json.loads(event.text)
          print(msg['price'])
          print(msg['type'])
          # self.processOBMessage(msg)
        except:
          print('couldnt parse msg')

if __name__ == '__main__':
  order_book = OrderBook('LTC-USD')
  # print(order_book.initial_ob)
  order_book.start()