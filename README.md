# gdax_OB
playing around with python for processing data from exchange over websockets

GDAX API reference: https://docs.gdax.com/

This branch removes all dependence on Node/MQTT that exists in master. Major dependence on the Python WS package we're using (which is pretty new).

Goals:
1. Use the GDAX WS API to construct a real-time OB with O(1) add/delete/modify (involves using the REST API to get initial OB state)
2. Use the GDAX REST API to retrieve trade history for specified products.
