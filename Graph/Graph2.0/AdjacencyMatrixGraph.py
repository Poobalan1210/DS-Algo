"""This module contains the implementation of graph using Adjacency Matrix
"""

class graph:
    """This class implements graph data structure using adjacency matrix
    """

    def __init__(self,total_vertices):
        self.adjacency_matrix=[[-1]*total_vertices for x in range(total_vertices)]
        self.numvertex=total_vertices
        self.vertices={}
        self.verticeslist=[0]*total_vertices

    def set_vertex(self,vtx,id):
        """This method is used so we can use alphabetical names also for graph indexes by 
        mapping them with numerical values
        """
        if 0<=vtx<self.numvertex:
            self.vertices[id]=vtx
            self.verticeslist[vtx]=id

    def set_edge(self,frm,to,weight=0):
        """This method finds the numerical index for the vertices and then use them to 
        store the edge and cost
        """

        frm=self.vertices[frm]
        to=self.vertices[to]
        self.adjacency_matrix[frm][to]=weight
        self.adjacency_matrix[to][frm]=weight #To be added for a symmetric graph

    def print_graph(self):
        """This method is used to print the graph adjacency matrix
        """

        for i in range(self.numvertex):
            for j in range(self.numvertex):
                print(f" {self.adjacency_matrix[i][j]}",end=" ")
            print("")

    def get_vertices(self):
        """This method returns the vertices as labeled by user
        """

        return self.verticeslist

    def get_edges(self):
        """This method returns the edges with weights
        """

        edges=[]
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if self.adjacency_matrix[i][j]!=-1:
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjacency_matrix[i][j]))
        return edges

    def get_matrix(self):
        """This method returns the adjacency matrix of graph
        """

        return self.adjacency_matrix

if __name__=="__main__":
    g=graph(6)
    g.set_vertex(0,"a")
    g.set_vertex(1,"b")
    g.set_vertex(2,"c")
    g.set_vertex(3,"d")
    g.set_vertex(4,"e")
    g.set_vertex(5,"f")
    g.set_edge('a','e',10)
    g.set_edge('a','c',20)
    g.set_edge('c','b',30)
    g.set_edge('b','e',40)
    g.set_edge('e','d',50)
    g.set_edge('f','e',60)
    print("Graph Vertices:")
    print(g.get_vertices())
    print("\nGraph Edges:")
    edges=g.get_edges()
    for edge in edges:
        print(edge)
    print("\nGraph Representation:")
    g.print_graph()
    print("\nGraph Matrix:")
    print(g.get_matrix())
    
    