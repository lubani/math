import random
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
matplotlib.use('TkAgg')  # Use a GUI-capable backend
# Constants for colors
WHITE, GRAY, BLACK = 0, 1, 2
COLOR_MAP = {WHITE: 'white', GRAY: 'gray', BLACK: 'black'}

class BFSAnimator:
    def __init__(self, num_nodes, num_edges):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.fig, self.ax = plt.subplots()
        self.G = self.generate_random_graph()
        self.pos = nx.spring_layout(self.G)
        self.anim = None

    def generate_random_graph(self):
        return nx.gnm_random_graph(self.num_nodes, self.num_edges)

    def bfs_with_animation(self, start_node):
        color = [WHITE] * self.num_nodes
        distance = [float('inf')] * self.num_nodes
        parent = [None] * self.num_nodes

        color[start_node] = GRAY
        distance[start_node] = 0
        queue = deque([start_node])

        frames = []

        def record_frame():
            color_map = [COLOR_MAP[c] for c in color]
            frames.append(color_map)

        record_frame()

        while queue:
            u = queue.popleft()
            for v in self.G.neighbors(u):
                if color[v] == WHITE:
                    color[v] = GRAY
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                    record_frame()
            color[u] = BLACK
            record_frame()

        return frames

    def draw_graph(self, color_map):
        nx.draw(self.G, self.pos, with_labels=True, node_color=color_map, node_size=500, edge_color='black', ax=self.ax)

    def animate_bfs(self, frames, filename="bfs_animation.gif"):
        def update(frame):
            self.ax.clear()
            self.draw_graph(frame)
            self.ax.set_title("BFS Animation")

        # Create the animation object
        self.anim = FuncAnimation(self.fig, update, frames=frames, repeat=False)

        # Save the animation to a file
        print("Saving animation...")
        self.anim.save(filename, writer='pillow')

        # Display the animation
        plt.show()

    def run(self):
        # Display the initial graph
        print("Initial random graph:")
        self.draw_graph(['white'] * self.num_nodes)
        plt.show()

        # Perform BFS and collect animation frames
        start_node = random.randint(0, self.num_nodes - 1)
        print(f"Starting BFS from node {start_node}:")
        frames = self.bfs_with_animation(start_node)

        # Animate BFS traversal and save the result
        print("Animating BFS traversal:")
        self.animate_bfs(frames)

if __name__ == "__main__":
    animator = BFSAnimator(num_nodes=10, num_edges=15)
    animator.run()
