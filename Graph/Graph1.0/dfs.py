"""This module contains the code to implement a depth first search algorithm on a graph"""

def dfs(graph,start_vertex,visited=None):
    """This function is used to run depth first search on a graph"""

    if visited is None:
        visited=set([])
    visited.add(start_vertex)
    print(start_vertex)
    for vertex in graph[start_vertex]-visited:
        dfs(graph,vertex,visited)
    return visited

if __name__=="__main__":
    gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }

    dfs(gdict,"a")
