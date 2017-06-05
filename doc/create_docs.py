import graphviz as gv
g1 = gv.Digraph(format='svg')

g1.edge('GDAX Server', 'Node.js ws client','OB msgs,heartbeat')
g1.edge('Node.js ws client', 'MQTT broker','publish')
g1.edge('Python MQTT client','MQTT broker','subscribe')

g1.render(filename='g1')
