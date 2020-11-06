class Trail:
    'Class for trail data'
    def __init__(self, name, distanceAway, length, elevation, description, latitude, longitude, difficulty):
        self._name = name
        self._distanceAway = distanceAway
        self._length = length
        self._elevation = elevation
        self._description = description
        self._latitude = latitude
        self._longitude = longitude
        self._difficulty = difficulty
        
    def getName(self):
        return self._name

    def getDistanceAway(self):
        return self._distanceAway
    
    def getLength(self):
        return self._length
           
    def getElevation(self):
        return self._elevation
            
    def getDescription(self):
        return self._description
            
    def getLatitude(self):
        return self._latitude
            
    def getLongitude(self):
        return self._longitude
                    
    def getDifficulty(self):
        return self._difficulty
            
    def setName(self, newName):
        self._name = newName
                    
    def setDistanceAway(self, newDistanceAway):
        self._distanceAway = newDistanceAway
                    
    def setLength(self, newLength):
        self._length = newLength
                    
    def setElevation(self, newElevation):
        self._elevation = newElevation
                    
    def setDescription(self, newDescription):
        self._description = newDescription
                    
    def setLatitude(self, newLatitude):
        self._latitude = newLatitude
                    
    def setLongitude(self, newLongitude):
        self._longitude = newLongitude
                            
    def setDifficulty(self, newDifficulty):
        self._difficulty = newDifficulty
        
 