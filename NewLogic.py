import regar

def plantCarrot(carrotLines):
	for i in range(carrotLines):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			plant(Entities.Carrot)
			regar.regar()
			move(North)
		move(East)

def plantTree(TreeLines):
	for i in range(TreeLines):
		for j in range(get_world_size()):
			if get_entity_type() == Entities.Tree:
				if can_harvest():
					harvest()	
					plant(Entities.Tree)	
			else:
				harvest()
			regar.regar()
			move(North)
		move(East)

def tillNonSoilGround():
	if get_ground_type() != Grounds.Soil:
		till()
		
def untillSoilGround():
	if get_ground_type() == Grounds.Soil:
		till()