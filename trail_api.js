var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

class Trail_API {
    constructor (latitude, longitude, distance = 10) {
        // User's latitude
        this._latitude = latitude;
        // User's longitude
        this._longitude = longitude;
        // Distance away from user trails will be found
        this._distance = distance;
        // Josh's Trail Data API key
        this._key = '200932678-b6a96c1d20b73dc70bee2145176ce8a7';
        // The full URL for the request
        this.url = `https://www.hikingproject.com/data/get-trails?lat=${this._latitude}&lon=${this._longitude}&maxDistance=${this._distance}&key=${this._key}`;
    }
    
    getTrails(){
        var request = new XMLHttpRequest();
        request.open('GET', this.url, true);
        request.onload = function () {
            console.log(request);
            if (request.status === 200){
                console.log(JSON.parse(request.response));
            } else {
                console.log(`error ${request.status} ${request.statusText}`);
            }
        };
        request.send();
    }

}

var la_latitude = 40.0274;
var la_longitude = -105.2519;
var myTrails = new Trail_API(la_latitude, la_longitude);
myTrails.getTrails();
