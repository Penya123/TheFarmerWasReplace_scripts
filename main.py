import getReady
import NewLogic
import SunFlowerLogic
import pumkinsLogicV2

# DESCRIPCIÓN DEL FLUJO
# Primero se plantan girasoles en 
# todo el campo y se cosechan 3 veces.
# Después se plantan y se consechan 
# calavazas 3 veces.
# Por último se cosecha se la manera clasica:
# 3 lineas de zanahorias y 9 de arboles y trigo
#
# Esto esta sujeto a cambios durante el desarrollo

clear()
wosi = get_world_size() # the world size
carrotRows = 10 # filas de zanahorias
treeRows = 12 # filas de arboles

while True:
	
	SunFlowerLogic.getSunflowerReady(wosi)
	SunFlowerLogic.farmSunflowers(1)
	
	getReady.getEverythingReady(carrotRows, treeRows)
	for i in range(3):
		NewLogic.plantCarrot(carrotRows)
		NewLogic.plantTree(treeRows)
	if num_items(Items.Fertilizer) >= (2 * get_world_size()):
		pumkinsLogicV2.plantPumkin(1)