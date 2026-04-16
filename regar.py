def regar(cantidadAgua):
	if cantidadAgua < 0.7 and get_entity_type() != Entities.Grass:
		return use_item(Items.Water)