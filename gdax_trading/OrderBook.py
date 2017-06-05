from operator import itemgetter
# from bintrees import RBTree
from decimal import Decimal
import queue

from gdax_trading.HTTPClient import HTTPClient
from lomond.websocket import WebSocket
import json

gdax_ws_endpoint='wss://ws-feed.gdax.com'

class OrderBook:
  initial_ob = None

  def __init__ (self, products):
    self.initial_ob = HTTPClient(products=products).getProductOrderBook(level=3,product=products)
    self.products = products
    # self._asks = RBTree()
    # self._bids = RBTree()
    self._sequence = -1

  def processOBMessage (self, message):
    sequence = message['sequence']

  def add (self, order):
    order = {
      'id': order['order_id'] if 'order_id' in order else order['id'],
      'side': order['side'],
      'price': Decimal(order['price']),
      'size': Decimal(order.get('size', order['remaining_size']))
    }

  def remove (self, order):
    price = Decimal(order['price'])
    if order['side'] == 'buy':
      bids = self.get_bids(price)
    else:
      asks = self.get_asks(price)

  def match (self, order):
    size = Decimal(order['size'])
    price = Decimal(order['price'])

    if order['side'] == 'buy':
      bids = self.get_bids(price)
      if not bids:
        return
      assert bids[0]['id'] == order['maker_order_id']
      if bids[0]['size'] == size:
        self.set_bids(price, bids[1:])
      else:
        bids[0]['size'] -= size
        self.set_bids(price, bids)
    else:
      asks = self.get_asks(price)
      if not asks:
        return
      assert asks[0]['id'] == order['maker_order_id']
      if asks[0]['size'] == size:
        self.set_asks(price, asks[1:])
      else:
        asks[0]['size'] -= size
        self.set_asks(price, asks)

  def change (self, order):
    new_size = Decimal(order['new_size'])
    price = Decimal(order['price'])

    if order['side'] == 'buy':
      bids = self.get_bids(price)
      if bids is None or not any(o['id'] == order['order_id'] for o in bids):
        return
      index = map(itemgetter('id'), bids).index(order['order_id'])
      bids[index]['size'] = new_size
      self.set_bids(price, bids)
    else:
      asks = self.get_asks(price)
      if asks is None or not any(o['id'] == order['order_id'] for o in asks):
        return
      index = map(itemgetter('id'), asks).index(order['order_id'])
      asks[index]['size'] = new_size
      self.set_asks(price, asks)

    tree = self._asks if order['side'] == 'sell' else self._bids
    node = tree.get(price)

    if node is None or not any(o['id'] == order['order_id'] for o in node):
      return

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
  order_book = OrderBook(["LTC-USD"])
  order_book.start()