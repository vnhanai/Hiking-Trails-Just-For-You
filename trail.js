
//class for storing longitude and latitude as a set
class Coordinates{
	constructor(longitude, latitude){
		this.longitude = longitude;
		this.latitude = latitude;
	}
	getLongitude(){
		return longitude;
	}
	getLatitude(){
		return latitude;
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
		var location = new Coordinates(longitude, latitude);
		this.difficulty = difficulty;
	}
	getName(){
		return name;
	}
	getDistanceAway(){
		return distanceAway;
	}
	getLength(){
		return length;
	}
	getElevation(){
		return elevation;
	}
	getDescription(){
		return description;
	}
	getLocation(){
		return location;
	}
	getDifficulty(){
		return difficulty;
	}
}

//class for the list of trails
class TrailList{
	constructor(){
		this.trails = trails[];
	}
	addTrail(newTrail){
			trails.push(newTrail);
	}
	getTrail(index){
		return trails[index];
	}
	deleteTrail(index){
		for(var i = index; i < trails.length-1; i++){
			trails[i] = trails[i+1];
		}
		trails.pop();
	}
	getLength()
	{
		return trails.length;
	}