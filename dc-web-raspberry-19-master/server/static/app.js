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
        document.getElementById('temp').innerHTML = response.temp;
    });
}

//setInterval(getTemp, 2000);

function getLight() {
    getURL('/api/light', function (result) {
        var response = JSON.parse(result);
        if(response.light < 200) {
            //Light mode
            document.body.style.backgroundColor = '#EEE';
        } else {
            //Dark mode
            document.body.style.backgroundColor = '#111';
        }
    });
}
//setInterval(getLight, 2000)

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