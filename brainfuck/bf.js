var brainfuck = require('brainfuck-javascript');
var md5 = require('md5');




var express = require('express');

var app = express();

cypherString = 'bpqaqabpmwzqoqvitntioGMAAAAABPMnTiOQaippipilpplpl'

app.get('/:bf', function(req, res) {
	bfCode = req.params.bf;
	console.log(bfCode)
    res.send( md5(brainfuck.text( bfCode, cypherString ))   );
});


app.listen(3000);
console.log('Express listening on port 3000...');


