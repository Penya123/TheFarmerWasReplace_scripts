import regar
import NewLogic

def getPumkinGroundReady(squareSize):
	for i in range(squareSize):
		for j in range(squareSize):
			harvest()
			NewLogic.tillNonSoilGround(get_ground_type())
			plant(Entities.Pumpkin)
			regar.regar(get_water())
			move(North)
		move(East)
		
def maintainPumkins(squareSize):
	for i in range(squareSize):
		for j in range(squareSize):
			if not can_harvest():
				plant(Entities.Pumpkin)
				regar.regar(get_water())	
			move(North)
		move(East)
		
def isPumkinCompleted(squareSize):
	for i in range(squareSize):
		for j in range(squareSize):
			if not can_harvest():
				return False	
			move(North)
		move(East)
	return True
	
