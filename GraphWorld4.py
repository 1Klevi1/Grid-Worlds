import heapq

# For this design there are 6 nodes described, like this: ["v1", "v2", "v3", "v4", "v5", "v6"]
# Everything is described using comments, just follow the instructions to run the tests. Yet again this design has used
# this paragraph, found in the worksheet 4, before we go on with task 1.

# We start with v1 as our first node. From here we will need to select the lowest edge, here 1 to v2.
# The next step is to select between the values {2,3,6,7} we select 2 to v3 as it is the lowest while not violating
# tree properties. Next is v4, followed by v6. This leaves us with {6 and 7} as edge values, but the 6 edge would
# lead to v6 and thus violate the tree properties. We have to select v5 via the 7 edge and we finish.
# So in my design we would have something like this :
# ('v1', 'v2', 1)
# ('v2', 'v3', 2)
# ('v1', 'v4', 3)
# ('v3', 'v6', 4)
# ('v2', 'v5', 7)
# Meaning -> (Vertex1, adjacent_Vertex2, edge)


class Graph:
    # Initialize the Graph class
    def __init__(self, agent):
        # Create the graph with its vertices and edges

        self.graph = {
            "v1": {"v2": 1, "v4": 3},
            "v2": {"v1": 1, "v5": 7, "v6": 6, "v3": 2},
            "v3": {"v2": 2, "v6": 4},
            "v4": {"v1": 3},
            "v5": {"v2": 7},
            "v6": {"v2": 6, "v3": 4},
        }
        # Set the starting vertex for the minimum spanning tree

        self.start_vertex = "v1"
        # Set the agent that will be used to build the minimum spanning tree

        self.agent = agent
        # Create empty lists to store the vertices and edges of the minimum spanning tree

        self.tree_vertices = []

        self.tree_edges = []
        # Add the starting vertex to the list of vertices of the minimum spanning tree

        self.tree_vertices.append(self.start_vertex)

    # Method to build the minimum spanning tree

    def tree(self):
        # Create a set to keep track of the vertices that have been seen

        seen_nodes = set()
        # Loop through all the nodes in the graph

        for node in self.graph:
            # Loop through all the edges and weights for the current node

            for edge, weight in self.graph[node].items():
                # If the edge is not already in the minimum spanning tree

                if (node, edge, weight) not in self.tree_edges:
                    # Add the edge to the minimum spanning tree

                    self.tree_edges.append((node, edge, weight))
                    # If the current node has not been seen before

                    if node not in seen_nodes:
                        # Add the node to the list of vertices of the minimum spanning tree

                        self.tree_vertices.append(node)
                        # Add the node to the agent

                        self.agent.add_vertex(node)
                        # Add the node to the set of seen nodes

                        seen_nodes.add(node)
                        # If the edge has not been seen before

                    if node not in seen_nodes:
                        # Add the edge to the list of vertices of the minimum spanning tree

                        self.tree_vertices.append(edge)
                        # Add the edge to the agent

                        self.agent.add_vertex(edge)
                        # Add the edge to the set of seen nodes

                        seen_nodes.add(edge)
                        # Add the edge to the agent

                    self.agent.add_edge((node, edge, weight))

    # Method to display the minimum spanning tree

    def display(self):
        # Loop through all the edges in the minimum spanning tree and print them

        for edge in self.tree_edges:
            print(edge[0], "->", edge[1], ":", edge[2])
        print()

    # Method to print the graph

    def print_graph(self):
        # Loop through all the vertices and their edges in the graph and print them

        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")
        print()


# Define the Agent class


class Agent:
    # Initialize the class attributes

    def __init__(self):
        self.tree_nodes = []
        self.tree_edges = []
        self.perceive_graph = {
            "v1": {"v2": 1, "v4": 3},
            "v2": {"v1": 1, "v5": 7, "v6": 6, "v3": 2},
            "v3": {"v2": 2, "v6": 4},
            "v4": {"v1": 3},
            "v5": {"v2": 7},
            "v6": {"v2": 6, "v3": 4},
        }
        self.current_node = "v1"
        self.seen_vertex = set()
        self.heap = []

    # Add a vertex to the tree

    def add_vertex(self, node):
        self.tree_nodes.append(node)

    # Add an edge to the tree

    def add_edge(self, edge):
        self.tree_edges.append(edge)

    # Get all the vertices in the tree

    def get_vertex(self):
        return "Vertices: ", self.tree_nodes

    # Get all the edges in the tree

    def get_edges(self):
        return "Vertex1, Vertex2, Edge: ", self.tree_edges

    # Get all the edges of the current node that the agent can see

    def get_edges_from_node(self, node):
        self.current_node = node
        edges = self.perceive_graph.get(self.current_node)
        return f"The current node that the agent can see is: {self.current_node}, followed by vertices and edges: {edges}"

    # Choose the edge with the lowest weight from the current vertex

    def choose_edge(self, vertex):
        lowest_edge = None
        lowest_weight = float("inf")
        self.seen_vertex.add(vertex)
        heap = []
        for adjacent_vertex, weight in self.perceive_graph[vertex].items():
            if adjacent_vertex not in self.seen_vertex:
                heapq.heappush(heap, (weight, vertex, adjacent_vertex))
        while heap:
            weight, v1, v2 = heapq.heappop(heap)
            if v2 not in self.seen_vertex:
                self.seen_vertex.add(v2)
                lowest_edge = (v1, v2, weight)
                break
        if lowest_edge is None:
            return None
        self.seen_vertex.add(lowest_edge[1])
        return lowest_edge

    # Move the agent to the next node
    def agent_walk(self, node):
        self.current_node = node
        next_edge = self.choose_edge(self.current_node)
        if next_edge is None:
            print("The agent can't go anywhere from node", self.current_node)
        else:
            print("Agent walking to:", next_edge)


a = Agent()
w = Graph(a)
# visualising our graph
print("Visualising our graph: ")
w.print_graph()
# spanning our tree, it's not supposed to print anything, the other function will deal with that "display"
w.tree()

# Vertices
print("Vertices: ")
print(a.get_vertex())
print()
# Vertex1, Vertex2, Edge
print("Vertex1, adjacent_Vertex2, Edge: ")
print(a.get_edges())
print()
# Agent's sensing functionality
print("Agent's sensing functionality: ")
current_node = a.current_node
print(a.get_edges_from_node(current_node))
print()
# Printing our spanning tree
print("Printing our spanning tree: ")
w.display()
#
print()
# Task 3 and 4, choosing the lowest edge, without creating loops, updated to use a heap as well, just uncomment this part
# But comment Task 5, I'm saying that because our agent has a memory

# print("Task 3 and 4\n")
# print(a.choose_edge(current_node))
# print(a.choose_edge("v2"))
# print(a.choose_edge("v1"))
# print(a.choose_edge("v3"))
# print(a.choose_edge("v2"))

# Task 5, to run this code please comment task 3, I'm saying that because our agent has a memory,
# to know if the result is ok You would need to read this part,
# it's the same thing for task 3 as well:

# We start with v1 as our first node. From here we will need to select the lowest edge, here 1 to v2.
# The next step is to select between the values {2,3,6,7} we select 2 to v3 as it is the lowest while not violating
# tree properties. Next is v4, followed by v6. This leaves us with {6 and 7} as edge values, but the 6 edge would
# lead to v6 and thus violate the tree properties. We have to select v5 via the 7 edge and we finish.
# So we would have something like this :
# ('v1', 'v2', 1)
# ('v2', 'v3', 2)
# ('v1', 'v4', 3)
# ('v3', 'v6', 4)
# ('v2', 'v5', 7)
# Meaning -> (Vertex1, adjacent_Vertex2, edge)
#
print("Task 5\n")
a.agent_walk(current_node)
print(a.get_edges_from_node(current_node))
a.agent_walk("v2")
print(a.get_edges_from_node("v2"))
a.agent_walk("v1")
print(a.get_edges_from_node("v1"))
a.agent_walk("v3")
print(a.get_edges_from_node("v3"))
a.agent_walk("v2")
print(a.get_edges_from_node("v2"))

# This is a test for task 5 to check the if statement, you can comment task 5 and proceed with the test
# a.agent_walk(current_node)
# print(a.get_edges_from_node(current_node))
# a.agent_walk("v2")
# print(a.get_edges_from_node("v2"))
# a.agent_walk("v3")
# print(a.get_edges_from_node("v3"))
# a.agent_walk("v6")
# print(a.get_edges_from_node("v6"))
# a.agent_walk("v4")
# print(a.get_edges_from_node("v4"))
