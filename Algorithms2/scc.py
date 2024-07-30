import random
import networkx as nx
import matplotlib.pyplot as plt


class SCCFinder:
    def __init__(self, num_nodes, num_edges):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.G = self.generate_random_directed_graph()
        self.GT = self.G.reverse()  # Transposed graph
        self.sccs = []
        self.visited = set()

    def generate_random_directed_graph(self):
        return nx.gnm_random_graph(self.num_nodes, self.num_edges, directed=True)

    def first_dfs(self):
        finish_stack = []
        visited = set()

        def dfs(v):
            visited.add(v)
            for neighbor in self.G.neighbors(v):
                if neighbor not in visited:
                    dfs(neighbor)
            finish_stack.append(v)

        for node in range(self.num_nodes):
            if node not in visited:
                dfs(node)

        return finish_stack

    def second_dfs(self, finish_stack):
        sccs = []
        visited = set()

        def dfs(v, scc):
            visited.add(v)
            scc.append(v)
            for neighbor in self.GT.neighbors(v):
                if neighbor not in visited:
                    dfs(neighbor, scc)

        while finish_stack:
            node = finish_stack.pop()
            if node not in visited:
                scc = []
                dfs(node, scc)
                sccs.append(scc)

        return sccs

    def find_sccs(self):
        # First pass on original graph
        finish_stack = self.first_dfs()

        # Second pass on transposed graph
        self.sccs = self.second_dfs(finish_stack)
        return self.sccs

    def draw_graph(self, G, node_colors=None, title=None):
        pos = nx.spring_layout(G)
        if node_colors is None:
            node_colors = 'lightblue'
        nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', node_size=500)
        if title:
            plt.title(title)
        plt.show()

    def draw_scc_graph(self):
        color_map = ['lightblue'] * self.num_nodes
        for i, scc in enumerate(self.sccs):
            color = plt.cm.rainbow(i / len(self.sccs))
            for node in scc:
                color_map[node] = color
        self.draw_graph(self.G, node_colors=color_map, title="Graph with SCCs Highlighted")

    def draw_scc_reduced_graph(self):
        # Create a reduced graph where each SCC is represented as a single node
        scc_graph = nx.DiGraph()
        scc_map = {node: idx for idx, scc in enumerate(self.sccs) for node in scc}
        for u, v in self.G.edges:
            if scc_map[u] != scc_map[v]:
                scc_graph.add_edge(scc_map[u], scc_map[v])

        # Draw the reduced SCC graph
        self.draw_graph(scc_graph, node_colors='lightgreen', title="Reduced Graph of SCCs")

    def run(self):
        # Draw the initial graph
        self.draw_graph(self.G, title="Original Graph")

        # Find SCCs
        self.find_sccs()

        # Draw the graph with SCCs highlighted
        self.draw_scc_graph()

        # Draw the reduced graph with SCCs
        self.draw_scc_reduced_graph()


if __name__ == "__main__":
    scc_finder = SCCFinder(num_nodes=10, num_edges=15)
    scc_finder.run()
