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
        response === "jour" ? document.body.style.backgroundColor = 'white' : document.body.style.backgroundColor = 'blue';        
    });
}

setInterval(getTemp, 2000);
setInterval(getLuminosite, 2000);