class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices in the graph
        self.graph = []  # Initialize an empty list to store edges

    def add_edge(self, u, v, w):
        """
        Add an undirected edge to the graph.

        Parameters:
        - u, v: vertices connected by the edge
        - w: weight of the edge
        """
        self.graph.append([u, v, w])  # Add the edge to the graph

    def find(self, parent, i):
        """
        Find the subset (or root) of an element i in the disjoint set.

        Parameters:
        - parent: list representing the parent of each element in the disjoint set
        - i: element whose root needs to be found

        Returns:
        - The root (subset representative) of element i
        """
        if parent[i] == i:  # If the element is its own parent, it's the root
            return i
        return self.find(parent, parent[i])  # Recursively find the root

    def apply_union(self, parent, rank, x, y):
        """
        Union two subsets based on their ranks.

        Parameters:
        - parent: list representing the parent of each element in the disjoint set
        - rank: list representing the rank (depth) of each subset's tree
        - x, y: elements (or subset representatives) to be merged
        """
        xroot = self.find(parent, x)  # Find the root of subset x
        yroot = self.find(parent, y)  # Find the root of subset y
        if rank[xroot] < rank[yroot]:  # If rank of x's tree is smaller, make y's root the parent
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:  # If rank of y's tree is smaller, make x's root the parent
            parent[yroot] = xroot
        else:  # If ranks are equal, arbitrarily choose one root as parent and increment its rank
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        """
        Apply Kruskal's algorithm to find the Minimum Spanning Tree (MST) of the graph.

        Kruskal's algorithm steps:
        1. Sort the edges of the graph by their weights.
        2. Initialize an empty result list to store MST edges.
        3. Create a disjoint set to keep track of subsets.
        4. Iterate through sorted edges and add them to MST if they don't form a cycle.
        5. Print the edges of the MST.
        """
        result = []  # Initialize an empty list to store MST edges
        i, e = 0, 0  # Initialize counters for edges and MST edges
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Sort edges by weight
        parent = []  # Initialize parent list for disjoint set
        rank = []  # Initialize rank list for disjoint set
        for node in range(self.V):
            parent.append(node)  # Each node is initially its own parent (root)
            rank.append(0)  # Rank of each subset is initially 0 (depth)
        while e < self.V - 1:  # Until MST has V-1 edges (where V is number of vertices)
            u, v, w = self.graph[i]  # Extract edge (u, v, w) from sorted graph
            i += 1  # Move to the next edge
            x = self.find(parent, u)  # Find root of subset containing u
            y = self.find(parent, v)  # Find root of subset containing v
            if x != y:  # If adding edge (u, v) doesn't create a cycle in MST
                e += 1  # Increment MST edge count
                result.append([u, v, w])  # Add edge (u, v, w) to MST
                self.apply_union(parent, rank, x, y)  # Union subsets containing u and v
        for u, v, weight in result:  # Print the edges of the MST
            print("%d - %d: %d" % (u, v, weight))

# Example usage
g = Graph(6)  # Create a graph with 6 vertices
# Add edges with corresponding weights
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()  # Apply Kruskal's algorithm to find Minimum Spanning Tree
