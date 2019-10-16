function getTemp()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", '/api/temperature', false ); // false for synchronous request
    xmlHttp.send( null );
    response = JSON.parse(xmlHttp.responseText);
    document.getElementById('tempC').innerText=response.celsius;
    document.getElementById('tempF').innerText=response.fahrenheit;
}

setInterval(getTemp,2000)