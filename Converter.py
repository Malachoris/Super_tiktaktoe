class Converter:
	
	@staticmethod
	def input_value_converter(list_of_values: list) -> list:
		
		numeric_values = []

		conversions = {
		"x": 1, 
		"o": -1
		}

		for value in list_of_values:
			numeric_values.append(conversions.get(value,0))


		return numeric_values
