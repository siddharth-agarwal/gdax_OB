/**
 * Created by sid on 5/26/17.
 */
var mqtt = require('mqtt')
var Gdax = require('gdax')

var client  = mqtt.connect('mqtt://127.0.01')

client.on('connect', function () {
  // client.subscribe('presence')
  client.publish('presence', 'stream starting')
})

var websocket = new Gdax.WebsocketClient(['BTC-USD', 'ETH-USD'])

websocket.on('message', function(data) {
    // var msg = JSON.parse(data);
    // console.log(data)
    // console.log(msg)
    client.publish('presence', JSON.stringify(data))
});

// client.on('message', function (topic, message) {
//   // message is Buffer
//   console.log(message.toString())
//   client.end()
// })
//

