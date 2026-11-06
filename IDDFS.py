#Find goal node G using IDDFS, starting from A.

class Graph:

    def __init__(self):
        self.adj = {}

    def addEdge(self, u, v):

        if u not in self.adj:
            self.adj[u] = []

        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append(v)

    # Depth Limited Search
    def DLS(self, start, goal, depth_limit):

        stack = [(start, 0, [start])]
        visited = []

        while stack:

            vertex, depth, path = stack.pop()
            visited.append(vertex)

            if vertex == goal:
                return path, visited

            if depth >= depth_limit:
                continue

            neighbours = self.adj.get(vertex, [])

            i = len(neighbours) - 1

            while i >= 0:

                neighbour = neighbours[i]

                if neighbour not in path:
                    stack.append(
                        (neighbour, depth + 1, path + [neighbour])
                    )

                i -= 1

        return None, visited

    # Iterative Deepening Search
    def IDDFS(self, start, goal, max_depth):

        print("\n========== ITERATIVE DEEPENING SEARCH ==========")
        print(f"Starting Node : {start}")
        print(f"Goal Node     : {goal}")
        print(f"Maximum Depth : {max_depth}")

        for limit in range(max_depth + 1):

            print(f"\nDepth Limit {limit}:")

            path, visited = self.DLS(start, goal, limit)

            print("Traversal:", " -> ".join(visited))

            if path is not None:

                print("\nGoal Found Successfully!")
                print("Final Path:", " -> ".join(path))
                return

        print("\nGoal Not Found!")


# Main Driver Code

if __name__ == "__main__":

    g = Graph()

    # Connect A with B, F, D and E.
    g.addEdge('A', 'B')
    g.addEdge('A', 'F')
    g.addEdge('A', 'D')
    g.addEdge('A', 'E')

    # Connect B with K and J.
    g.addEdge('B', 'K')
    g.addEdge('B', 'J')

    # Connect K with N and M.
    g.addEdge('K', 'N')
    g.addEdge('K', 'M')

    # Connect D with G.
    g.addEdge('D', 'G')

    # Connect E with C, H and I.
    g.addEdge('E', 'C')
    g.addEdge('E', 'H')
    g.addEdge('E', 'I')

    # Connect I with L.
    g.addEdge('I', 'L')

    # Run IDDFS with maximum depth 3.
    g.IDDFS('A', 'G', 3)