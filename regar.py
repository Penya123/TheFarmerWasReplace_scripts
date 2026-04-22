def regar():
	if get_water() < 0.5 and get_entity_type() != Entities.Grass:
		return use_item(Items.Water)