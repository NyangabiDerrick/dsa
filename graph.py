# By Ericson Karanja
# Graph - Nodes (vertices) connected by edges
# BFS traversal: O(V + E) where V=vertices, E=edges

from collections import defaultdict, deque

class Graph:
    """Graph implementation using adjacency list"""
    def __init__(self):
        # Adjacency list: key=node, value=list of neighbors
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Add an undirected edge between nodes u and v"""
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def bfs(self, start):
        """Breadth-First Search starting from given node"""
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()  # Dequeue from front
            print(node, end=" ")
            
            # Add unvisited neighbors to queue
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    print("BFS from node 0:")
    g.bfs(0)
    print()
