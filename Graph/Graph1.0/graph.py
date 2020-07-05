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

	def get_vertices(self):
		"""This method returns the vertices of the graph"""

		return list(self.gdict.keys())

	def get_edges(self):
		"""This method returns all the unique edges of the graph"""
		
		edge_list=[]
		for vertex in self.gdict:
			for next_vertex in self.gdict[vertex]:
				if {vertex,next_vertex} not in edge_list:
					edge_list.append({vertex,next_vertex})
		return edge_list

	def add_vertex(self,new_vertex):
		"""This method is used to add a new vertex in the graph"""
		
		self.gdict[new_vertex]=[]

	def add_edge(self,edge):
		"""This method is used to add an edge inside the graph"""

		vertex1,vertex2=tuple(edge)
		if vertex1 in self.gdict:
			self.gdict[vertex1].append(vertex2)
		else:
			self.gdict[vertex1]=[vertex2]
		
		if vertex2 not in self.gdict:
			self.gdict[vertex2]=[]

if __name__=="__main__":
	sample_dict = { "a" : ["b","c"],
			"b" : ["a","d"],
			"c" : ["a","d"],
 			"d" : ["b","c"],
			"e" : ["d"]
		      }
	
	#Making graph object
	graph_obj = Graph(sample_dict)

	#Printing the internal dictionary of graph
	print("The Graph dict is: ", end=" ")
	graph_obj.print_graph()
	
	#Getting the Graph vertices
	print(f"\nThe Graph vertices are: {graph_obj.get_vertices()} \n")

	#Getting the Graph edges
	print(f"The Graph edges are: {graph_obj.get_edges()} \n")

	#Adding new Vertex in Graph
	graph_obj.add_vertex("f")
	print(f"The updated vertices of Graph is: {graph_obj.get_vertices()} \n")

	#Adding new edges in Graph
	graph_obj.add_edge(("a","e"))
	graph_obj.add_edge(("f","g"))
	print(f"The updated graph is: ",end="\n")
	graph_obj.print_graph()