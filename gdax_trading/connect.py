import paho.mqtt.subscribe as subscribe

def print_msg (client, userdata, message):
  print("%s : %s" % (message.topic, message.payload))


subscribe.callback(callback=print_msg,topics='presence',hostname='localhost')