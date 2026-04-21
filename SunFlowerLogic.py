import NewLogic
import regar

def getSunflowerReady(sunflowerLines):
	for i in range(sunflowerLines):
		for j in range(get_world_size()):
			harvest()
			NewLogic.tillNonSoilGround(get_ground_type())
			plant(Entities.Sunflower)
			regar.regar(get_water())
			move(North)
		move(East)

def farmSunflowers(timesFarmingSunflowers):
	for i in range(timesFarmingSunflowers):
		for j in range(get_world_size()):
			for k in range(get_world_size()):
				if measure() == 15:
					harvest()
					plant(Entities.Sunflower)
				else:
					NewLogic.untillSoilGround(get_ground_type())
					till()
					plant(Entities.Sunflower)
				regar.regar(get_water())
				move(North)
			move(East)