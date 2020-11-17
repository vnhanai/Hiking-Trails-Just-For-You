
//class for storing longitude and latitude as a set
class Coordinates{
	constructor(longitude, latitude){
		this.longitude = longitude;
		this.latitude = latitude;
	}
	getLongitude(){
		return this.longitude;
	}
	getLatitude(){
		return this.latitude;
	}
}

//class for storing trail data
class Trail{
	constructor(name, distanceAway, length, elevation, description, longitude, latitude, difficulty){
		this.name = name;
		this.distanceAway = distanceAway;
		this.length = length;
		this.elevation = elevation;
		this.description = description;
		this.location = new Coordinates(longitude, latitude);
		this.difficulty = difficulty;
	}
	getName(){
		return this.name;
	}
	getDistanceAway(){
		return this.distanceAway;
	}
	getLength(){
		return this.length;
	}
	getElevation(){
		return this.elevation;
	}
	getDescription(){
		return this.description;
	}
	getLocation(){
		return this.location;
	}
	getDifficulty(){
		return this.difficulty;
	}
}

//class for the list of trails
class TrailList{
	constructor(){
		this.trails = [];
	}
	addTrail(newTrail){
			this.trails.push(newTrail);
	}
	getTrail(index){
		return this.trails[index];
	}
	deleteTrail(index){
		for(var i = index; i < trails.length-1; i++){
			this.trails[i] = this.trails[i+1];
		}
		trails.pop();
	}
	getLength(){
		return trails.length;
	}
}

module.exports.Coordinates = Coordinates;
module.exports.Trail = Trail;
module.exports.TrailList = TrailList;