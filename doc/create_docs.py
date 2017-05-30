import graphviz as gv
g1 = gv.Digraph(format='svg')

g1.edge('GDAX Server', '(local) ws connection','OB msgs,heartbeat')
g1.edge('(local) ws connection', '(local) MQTT broker','MQTT publish')
g1.edge('Python MQTT client','(local) MQTT broker','MQTT subscribe')

g1.render(filename='g1')
