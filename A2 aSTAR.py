def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parent = {start_node: start_node}
    
    while len(open_set) > 0:
        n = None
        
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        
        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for m, weight in get_neighbours(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parent[m] = n
                    g[m] = g[n] + weight
                
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parent[m] = n
                        
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
                            
        if n is None:
            print("Path does not exist!")
            return None
        
        if n == stop_node:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start_node)
            path.reverse()
            print("Path found: {}".format(path))
            return path
        
        open_set.remove(n)
        closed_set.add(n)
    print("Path does not exist!")
    return None

def get_neighbours(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    
def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist[n]

Graph_nodes = {'A': [('B', 2), ('E', 3)], 'B': [('A', 2), ('C', 1), ('G', 9)], 'C': [('B', 1)], 'D': [('E', 6), ('G', 1)], 'E': [('A', 3), ('D', 6)], 'G': [('B', 9), ('D', 1)]}

start_node = input("Enter start node: ")
stop_node = input("Enter stop node: ")
aStarAlgo(start_node, stop_node)
