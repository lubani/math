import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


def generate_random_dag(num_nodes, num_edges):
    """Generate a random Directed Acyclic Graph (DAG)"""
    G = nx.DiGraph()

    # Add nodes
    G.add_nodes_from(range(num_nodes))

    # Add edges randomly ensuring acyclic property
    while len(G.edges) < num_edges:
        u, v = random.sample(range(num_nodes), 2)
        if u != v and not G.has_edge(u, v) and not G.has_edge(v, u):
            G.add_edge(u, v)
            # Ensure no cycles are formed
            if not nx.is_directed_acyclic_graph(G):
                G.remove_edge(u, v)

    return G


def kahn_topological_sort(G):
    """Perform Kahn's Algorithm for topological sorting"""
    in_degree = {u: 0 for u in G.nodes()}
    for u, v in G.edges():
        in_degree[v] += 1

    # Collect all nodes with zero in-degree
    zero_in_degree = [u for u in G.nodes() if in_degree[u] == 0]
    topological_order = []
    steps = []

    while zero_in_degree:
        current = zero_in_degree.pop(0)
        topological_order.append(current)
        steps.append(list(topological_order))  # Record the current state for animation

        for neighbor in G.successors(current):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    if len(topological_order) == len(G.nodes()):
        return topological_order, steps
    else:
        raise ValueError("Graph is not acyclic")


def update(frame, G, pos, ax, steps):
    ax.clear()
    ax.set_title(f"Topological Sort Step {frame + 1}")

    # Draw the entire graph
    nx.draw_networkx(G, pos, ax=ax, node_color='lightblue', edge_color='gray', with_labels=True, arrows=True)

    # Highlight nodes in topological order up to the current step
    sorted_nodes = steps[frame]
    node_colors = ['orange' if node in sorted_nodes else 'lightblue' for node in G.nodes()]

    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors)


def main():
    random.seed(42)

    # Generate a random DAG
    num_nodes = 10
    num_edges = 15
    G = generate_random_dag(num_nodes, num_edges)

    # Perform topological sort using Kahn's Algorithm
    try:
        topological_order, steps = kahn_topological_sort(G)
        print(f"Topological Order: {topological_order}")

        # Set up the plot
        pos = nx.spring_layout(G)
        fig, ax = plt.subplots()

        # Create an animation for the topological sorting
        ani = FuncAnimation(fig, update, frames=len(steps), fargs=(G, pos, ax, steps), repeat=False)
        ani.save('topological_sort_animation.gif', writer='pillow')

        # Show the plot
        plt.show()

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
