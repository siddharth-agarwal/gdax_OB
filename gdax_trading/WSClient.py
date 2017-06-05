from lomond.websocket import WebSocket
import json
from threading import Thread

gdax_ws_endpoint='wss://ws-feed.gdax.com'
# subscribe_msg={"type": "subscribe","product_ids": ["LTC-USD"]}

class WSClient(object):

    def __init__(self, products):
      self.products = products
      self.thread = None

    def start(self):
      def go():
        sub_params = {'type': 'subscribe', 'product_ids': self.products}
        ws = WebSocket(gdax_ws_endpoint)

        for event in ws.connect():
          if event.name == 'poll':
            ws.send_text(json.dumps(sub_params))
          elif event.name == 'text':

            # print(event.text)

            try:
              msg = json.loads(event.text)
              print(msg['price'])
              print(msg['type'])
            except:
              print('couldnt parse msg')

      Thread(target=go).start()

if __name__ == "__main__":
    wsClient = WSClient(products=["LTC-USD"])
    wsClient.start()