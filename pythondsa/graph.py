class Graph:
    def __init__(self):
        self.graph = {}

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add an edge to the graph (undirected)
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        else:
            print("One or both vertices not found.")

    # Depth-First Search (DFS)
    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=' ')
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Breadth-First Search (BFS)
    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    # Print the graph
    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    print("Graph:")
    g.print_graph()
    
    print("\nDFS starting from vertex 0:")
    g.dfs(0)  # Output: 0 1 2 3
    
    print("\n\nBFS starting from vertex 0:")
    g.bfs(0)  # Output: 0 1 2 3
