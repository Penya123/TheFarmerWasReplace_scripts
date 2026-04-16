import regar

def plantCarrot(carrotLines):
	for i in range(carrotLines):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			plant(Entities.Carrot)
			regar.regar(get_water())
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
			regar.regar(get_water())
			move(North)
		move(East)
