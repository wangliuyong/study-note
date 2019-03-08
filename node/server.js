var http = require('http');
var fs = require('fs');
var data = fs.readFileSync('./data');

http.createServer(function (req, res) {

    if(req.url){
        console.log(req.url)
    }else{
        console.log('no path')
    }

    res.writeHead(200, {
        'Content-Length': data.length,
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin':'*'
    });

    res.end(data);
}).listen(80);



