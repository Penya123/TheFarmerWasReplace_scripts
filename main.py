import getReady
import NewLogic

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
carrotRows = 3
treeRows = 9
getReady.getEverythingReady(carrotRows,treeRows)

while True:
	NewLogic.plantCarrot(carrotRows)
	NewLogic.plantTree(treeRows)
