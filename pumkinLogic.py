import regar

def plantPumkin(squareSize):
	for i in range(squareSize):
		for j in range(squareSize):
			if not get_ground_type() == Grounds.Soil:
				till()
				regar.regar(get_water())
			while True:
				if can_harvest():
					break
				plant(Entities.Pumpkin)
			move(North)
			if get_pos_y() >= squareSize:
				while True:
					move(North)
					if get_pos_y() >= (get_world_size() - 1):
						move(North)
						break
		if i >= (squareSize - 1):
			harvest()
			move(East)
			break
		else:
			move(East)


def getPumkinGroundReady(squareSize):
	for i in range(squareSize):
		for j in range(squareSize):
			till()
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
	
