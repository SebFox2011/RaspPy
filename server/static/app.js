function getURL(url, success) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            success(xmlHttp.responseText);
        }
    }
    xmlHttp.open("GET", url, true);
    xmlHttp.send();
}

function getTemp() {
    getURL('/api/temperature', function (result) {
        var response = JSON.parse(result);
        document.getElementById('tempC').innerText=response.celsius;
        document.getElementById('tempF').innerText=response.fahrenheit;
    });
}

function getLuminosite() {
    getURL('/api/luminosite', function (result) {
        var response = JSON.parse(result);
        document.getElementById('luminosite').innerText=response;
        console.log(response);
        response === "jour" ? document.body.style.backgroundColor = 'white' : document.body.style.backgroundColor = 'black';        
    });
}

setInterval(getTemp, 2000);
setInterval(getLuminosite, 2000);

$(function () {
	socket = io.connect('http://' + document.domain + ':' + location.port);
	socket.on('connect', function() {
		$('#status').text('Connecté');
        socket.emit('client_connected', {data: 'New client!'});
	});

	socket.on('disconnect', function() {
		$('#status').text('Déconnecté');
	});

	socket.on('alert', function (data) {
        $('#status').text('Connecté');
        $('#content').append(data + "<br />");
	});
});