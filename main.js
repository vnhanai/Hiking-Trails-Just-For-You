var express = require('express');
const path = require('path');

//const Trail_API = require('./trail_api.js').Trail_API;
// ** This Trail_API is mock data because we were locked out of the API **
const Trail_API = require('./local_trail_api.js').Trail_API;

//use express handlebars
var app = express();

//add data parsers
app.use(express.urlencoded());
app.use(express.json());

var handlebars = require('express-handlebars').create({defaultLayout:'main'});

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 3000);


//establish static page for js and css files
app.use(express.static(path.join(__dirname, 'static')));

//load user page as home display
app.get('/',function(req, res){
  res.render('user');
});

//load Trail display page
app.get('/trails',function(req, res){
  la_latitude = 40.0274;
  la_longitude = -105.2519;
  //Default location is LA
  // Rendering the page in this way allows the trailList to be accessed with the trailList variable
  res.render('trails', {"trailList": newLocation(la_latitude, la_longitude)});
});

//load Trail display after new location input
//apply difficulty from 'Just For You' filter
//need to convert zipcode to latlong
app.post('/trails',function(req,res){
  if (req.body.zipcode) {
    zipcode = req.body.zipcode;
    console.log("request zip code: ", zipcode);
  }
  if (req.body.difficulty) {
    request_diff = req.body.difficulty;
    console.log("requested difficulty: ", request_diff);
  }

  la_latitude = 40.0274;
  la_longitude = -105.2519;

  res.render('trails', {"trailList": newLocation(la_latitude, la_longitude)});
});

//error status 404
app.use(function(req,res){
  res.status(404);
  res.render('404');
});


//error 505
app.use(function(err, req, res, next){
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.render('500');
});

//display page on localhost:3000
app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});

//ping the API for the location of the trail and return the trailList
function newLocation(latitude,longitude) {
  const myTrails = new Trail_API(latitude, longitude);
  return myTrails.getTrails();
}


var csv = require('csv-parse');

function searchCSV(zipcode) {
  const output = [];

  const parser = csv({
    delimiter: ';';
  })

  parser.on('readable', function() {
    let record;
    while (record = parser.read()) {
      output.push(record);
    }
  })

  parser.on('error', function(err) {
    console.error(err.message);
  })

  for item in output {
    if 
  }
  return latitude, longitude;
}
