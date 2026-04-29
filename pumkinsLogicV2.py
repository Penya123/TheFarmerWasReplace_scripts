import regar
import NewLogic

def plantPumkin(times):
	for i in range(times):	
		for j in range(get_world_size()):
			for k in range(get_world_size()):
				harvest()
				NewLogic.tillNonSoilGround()
				regar.regar()
				while not can_harvest():
					plant(Entities.Pumpkin)
					if random() > 0.5:
						use_item(Items.Fertilizer)
				move(North)
			move(East)
		harvest()
