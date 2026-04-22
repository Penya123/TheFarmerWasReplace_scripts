import NewLogic

def getEverythingReady(carrotLines, TreeLines):
	getCarrotsReady(carrotLines)
	getTreesReady(TreeLines)


def getCarrotsReady(carrotLines):
	for i in range(carrotLines):
		for j in range(get_world_size()):
			NewLogic.tillNonSoilGround()
			plant(Entities.Carrot)
			move(North)
		move(East)
	
def getTreesReady(TreeLines):
	for i in range(TreeLines):
		for j in range(get_world_size()):
			NewLogic.untillSoilGround()
			if get_pos_y() % 2 == 0 and get_pos_x() % 2 != 0:
				plant(Entities.Tree)
			elif get_pos_y() % 2 != 0 and get_pos_x() % 2 == 0:
				plant(Entities.Tree)
			move(North)
		move(East)