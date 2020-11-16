
// import Trail, TrailList from Trail;
var https = require('https');

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

    makeTrailList(trailData){
        var trails = trailData.trails;
        for (var i = 0; i < trails.length; i++) {
            // Trails arguments (name, distanceAway, length, elevation, description, latitude, longitude, difficulty)
            console.log(trails[i].name,
            trails[i].longitude,
            trails[i].latitude,
            trails[i].length,
            trails[i].summary,
            trails[i].difficulty,
            
            trails[i].conditionStatus,
            trails[i].conditionDetails);
        }

    }
    
    getTrails(){
        // Returns a TrailList object
        https.get(this.url, res => {
            var data = '';
            
            res.on('data', chunk => {
                data += chunk;
            });

            res.on('end', ()=> {
                this.makeTrailList(JSON.parse(data));
            });         
        }).end();
    }

}

var la_latitude = 40.0274;
var la_longitude = -105.2519;
var myTrails = new Trail_API(la_latitude, la_longitude);
myTrails.getTrails();
