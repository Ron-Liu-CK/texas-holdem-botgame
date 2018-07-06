var playerClient = require('./modules/playerclient.js');
var player = require('./botplayer.js').botplayer;

// Cygni poker server:
//playerClient.connect('poker.cygni.se', 4711, player);
const args = process.argv;
var host = args[2];
var port = parseInt(args[3]);
playerClient.connect(host, port, player);
playerClient.playAGame(playerClient.ROOM_TRAINING());
