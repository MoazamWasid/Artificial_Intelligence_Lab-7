# Find goal node G using DLS, starting from A.

class Graph:

    def __init__(self):
        # Store nodes and their connected neighbours.
        self.adj = {}

    def addEdge(self, u, v):

        # Create an empty list if node does not exist.
        if u not in self.adj:
            self.adj[u] = []

        if v not in self.adj:
            self.adj[v] = []

        # Connect node u with node v.
        self.adj[u].append(v)

    def DLS(self, start, goal, depth_limit):

        # Stack stores node, depth and current path.
        stack = [(start, 0, [start])]

        print("\n========== DEPTH LIMITED SEARCH ==========")
        print(f"Starting Node : {start}")
        print(f"Goal Node     : {goal}")
        print(f"Depth Limit   : {depth_limit}")
        print("\nTraversal Order:")

        # Continue searching while stack is not empty.
        while stack:

            # Remove the last inserted element.
            vertex, depth, path = stack.pop()

            # Display the current visited node.
            print(vertex, end=" -> ")

            # Check if the goal node is reached.
            if vertex == goal:

                print("\n\nGoal Found Successfully!")
                print("Final Path:", " -> ".join(path))
                print("Path Length:", len(path) - 1, "edges")
                return

            # Stop expanding nodes beyond the depth limit.
            if depth >= depth_limit:
                continue

            # Get all connected neighbours.
            neighbours = self.adj.get(vertex, [])

            # Visit neighbours in reverse order.
            i = len(neighbours) - 1

            while i >= 0:

                neighbour = neighbours[i]

                # Avoid revisiting nodes in the current path.
                if neighbour not in path:

                    stack.append(
                        (neighbour, depth + 1, path + [neighbour])
                    )

                i -= 1

        # Display message if goal is not reached.
        print("\n\nGoal Not Found!")
        print("Depth limit reached without finding the goal.")


# Main Driver Code

if __name__ == "__main__":

    # Create graph object.
    g = Graph()

    # Connect A with its neighbours.
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

    # Connect D with goal node G.
    g.addEdge('D', 'G')

    # Connect E with C, H and I.
    g.addEdge('E', 'C')
    g.addEdge('E', 'H')
    g.addEdge('E', 'I')

    # Connect I with L.
    g.addEdge('I', 'L')

    # Execute Depth Limited Search.
    g.DLS('A', 'G', 1)