import getReady
import NewLogic

clear()
carrotRows = 3
treeRows = 9
getReady.getEverythingReady(carrotRows,treeRows)

while True:
	NewLogic.plantCarrot(carrotRows)
	NewLogic.plantTree(treeRows)
