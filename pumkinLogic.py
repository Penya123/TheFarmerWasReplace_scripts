import regar
import NewLogic

# Cambio de flujo:
#Un ciclo que todas las pumkin que esten buenas
#cuando encuentre una que no, le echará fertilizante
#y si es buena la deja ahí y se suma +1 al contador,
#si no, se repite
#cuando el contador sea igual a get_world_size()
#se cosechará todo

def getPumkinGroundReady(squareSize):
	for i in range(squareSize):
		for j in range(squareSize):
			harvest()
			NewLogic.tillNonSoilGround()
			plant(Entities.Pumpkin)
			regar.regar()
			move(North)
		move(East)
		
def maintainPumkins(squareSize):
	for i in range(squareSize):
		for j in range(squareSize):
			if not can_harvest():
				plant(Entities.Pumpkin)
				regar.regar()	
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
	
