class Forlayo:

	def prueba (self, rdd):
		return (rdd.flatMap(lambda x: x.split(" ")))