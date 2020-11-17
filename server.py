var express = require('express');

var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 3000);

app.get('/',function(req,res){
  res.render('user_page')
});

app.get('/trails',function(req,res){
  la_latitude = 40.0274
  la_longitude = -105.2519
  # Default location is LA
  myTrails = Trail_API(la_latitude, la_longitude)
  res.render('trails');
});

app.post('/trails',function(req,res){
  res.render('trails',newLocation())
});

app.use(function(req,res){
  res.status(404);
  res.render('404');
});

app.use(function(err, req, res, next){
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.render('500');
});

app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});

function newLocation() {
  latitude = 0
  longitude = 0
  myTrails = Trail_API(latitude, longitude)
  trails = myTrails.getTrails()
}