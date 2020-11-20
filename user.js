//starter code pulled from sessions homework in web_dev, written by me

var express = require('express');
var bodyParser = require('body-parser');
var session = require('express-session');   // how we will save user

var app = express();
//handlebars to handle templating
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
//session starting
app.use(session({secret:'SuperSecretPassword'}));

//bodyParser is important for post methods
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 53826);

//get function -- still needs to be rewritten for the user bit,
//but probably better applied to the trail recommendation
app.get('/',function(req,res){
  var context = {};
  context.count = req.session.count || 0;
  req.session.count = context.count + 1;
  res.render('counter', context);
});

//this code is left over from another assignment
/*
resetButton.addEventListener("click", e => {
  req.session.count = 0;
})*/

//this post function will need to be rewritten to parse and
//save as a "user"
app.post('/', function(req,res){
    var qParams = "";
    for (var p in req.query){
      qParams += "POST request received: " + req.query[p];
    }

    var context = {};
    context.dataList = qParams;
    res.render('home', {context : qParams});
  });
  
app.use(function(req,res){
  res.type('text/plain');
  res.status(404);
  res.send('404 - Not Found');
});

app.use(function(err, req, res, next){
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.send('500 - Server Error');
});

//need to find a port to operate off of
app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});

/* modified from code put together by Ai Vu, and updated to adjust for
return types independent of strings */

let User = class {
    constructor(age, height, weight, exercise_time, exercise_days,
        hiking_exp, health_assess) {
            //age = user age
            this.age = age;
            //height = user height in inches
            this.height = height;    
            //weight = user weight in pounds
            this.weight = weight;
            //exercise_time = user reported avg length of workout
            this.exercise_time = exercise_time;
            //exercise_days = user reported avg days worked out per week
            this.exercise_days = exercise_days;
            //hiking_exp = user reported hiking exp (bool type)
            this.hiking_exp = hiking_exp;
            //health_assess = user reported assessment of health
            this.health_assess = health_assess;
    }

    // Getter for BMI
    get bmi() {
        return this.calcBMI();
    }
    // the method that will calculate BMI
    calcBMI() {
        return this.weight / this.height;
    }
};


