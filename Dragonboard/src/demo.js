var net = require('net');

var client = new net.Socket()
client.connect(1236, "172.16.243.226", function(){

    client.write('{"sender": "Tim", "content" : "Message is this"}');


});

client.on('data', function(data) {
	console.log('Received: ' + data);
	client.destroy();
});
