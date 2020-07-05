'''This module contains the code to create a Graph class and also tests it 
'''

class Graph:
	'''This class is used to make a blueprint of a Graph
	'''
	
	def __init__(self,gdict=None):
		"""Constructor to create Graph object,
		it takes a default argument set to None,
		to take the graph dictionary"""

		if gdict is None:
			gdict = []
		self.gdict = gdict

	def print_graph(self):
		"""The dictionary holding the graph values is printed
		"""

		print(self.gdict)

if __name__=="__main__":
	sample_dict = { "a" : ["b","c"],
			"b" : ["a","d"],
			"c" : ["a","d"],
 			"d" : ["b","c"],
			"e" : ["d"]
		      }
	graph_obj = Graph(sample_dict)
	graph_obj.print_graph()