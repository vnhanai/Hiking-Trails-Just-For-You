from trail import Trail, TrailList

aTrail = Trail(name="Test Trail 1", difficulty=3, distanceAway=8.02, length=1.2, elevation=-0.8, description="testing printTrail", latitude=23.003, longitude=-34.043)

aTrail.printTrail()
#Test Trail 1

trailList = TrailList(aTrail)

aTrail = Trail(name="Test Trail 2", difficulty=5, distanceAway=4, length=2, elevation=1, description="testing TrailList", latitude=3, longitude=4)

trailList.addTrail(aTrail)

trailList.printList()
#Test Trail 1
#Test Trail 2

aTrail = trailList.getTrail(0)
aTrail.setDescription("testing getTrail and setDescription")
aTrail.printTrail()
#Test Trail 1

trailList.deleteTrail(0)
trailList.getTrail(0).setDescription("testing deleteTrail")

trailList.printList()
#Test Trail 2
