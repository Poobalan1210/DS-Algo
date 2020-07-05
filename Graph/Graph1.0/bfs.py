"""This module contains the code to implement a breadth first search algorithm on a graph"""

import collections

def bfs(graph,start_vertex):
    """This function is used to run breadth first search on a graph"""

    visited,queue=[start_vertex],collections.deque([start_vertex])

    while queue:
        current_vertex=queue.popleft()
        marked(current_vertex)
        
        for vertex in graph[current_vertex]:
            if vertex not in visited:
                visited.append(vertex)
                queue.append(vertex)

def marked(vertex):
    """This function marks a vertex to be visited by printing it"""

    print(vertex)

if __name__=="__main__":
    gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }

    bfs(gdict,"a")
