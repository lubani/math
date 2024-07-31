import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def bfs(G, s, t, parent):
    visited = {s}
    queue = [s]
    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if v not in visited and G[u][v]['capacity'] - G[u][v]['flow'] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == t:
                    return True
    return False


def ford_fulkerson(G, s, t):
    flow = 0
    parent = {}
    steps = []  # To record the flow at each step

    while bfs(G, s, t, parent):
        path_flow = float('Inf')
        v = t

        # Find the maximum flow through the path found by BFS
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, G[u][v]['capacity'] - G[u][v]['flow'])
            v = parent[v]

        print(f"Found path with available flow: {path_flow}")

        # Update residual capacities of the edges and reverse edges along the path
        v = t
        while v != s:
            u = parent[v]
            G[u][v]['flow'] += path_flow
            # Ensure the reverse edge exists; if not, add it with zero capacity
            if (v, u) not in G.edges():
                G.add_edge(v, u, capacity=0, flow=0)
            G[v][u]['flow'] -= path_flow
            v = parent[v]

        flow += path_flow

        # Debugging print for current flow state
        current_flow_state = {(u, v): G[u][v]['flow'] for u, v in G.edges() if G[u][v]['capacity'] > 0}
        print(f"Current flow state: {current_flow_state}")

        # Record the current state of flows
        steps.append(current_flow_state)

        # Print residual graph state
        print("Residual graph state after flow update:")
        print_residual_graph(G)

    return flow, steps


def create_random_network(nodes, edges, source, sink):
    G = nx.DiGraph()

    # Initial random connections
    while len(G.edges()) < edges:
        u = random.choice(range(nodes))
        v = random.choice(range(nodes))
        if u != v and not G.has_edge(u, v) and not (u == sink or v == source):
            capacity = random.randint(5, 20)
            G.add_edge(u, v, capacity=capacity, flow=0)
            G.add_edge(v, u, capacity=0, flow=0)  # Adding the reverse edge with 0 capacity

    # Ensure source has at least two outgoing edges with significant capacities
    outgoing_from_source = list(G.successors(source)) if source in G else []
    while len(outgoing_from_source) < 2:
        v = random.choice([node for node in range(nodes) if node != source and node != sink and node not in outgoing_from_source])
        capacity = random.randint(10, 20)
        if not G.has_edge(source, v):
            G.add_edge(source, v, capacity=capacity, flow=0)
            G.add_edge(v, source, capacity=0, flow=0)
            outgoing_from_source.append(v)

    # Ensure sink has at least two incoming edges with significant capacities
    incoming_to_sink = list(G.predecessors(sink)) if sink in G else []
    while len(incoming_to_sink) < 2:
        u = random.choice([node for node in range(nodes) if node != source and node != sink and node not in incoming_to_sink])
        capacity = random.randint(10, 20)
        if not G.has_edge(u, sink):
            G.add_edge(u, sink, capacity=capacity, flow=0)
            G.add_edge(sink, u, capacity=0, flow=0)
            incoming_to_sink.append(u)

    # Ensure intermediate nodes have multiple connections
    for node in range(nodes):
        if node not in (source, sink):
            connections = list(G.successors(node)) if node in G else []
            while len(connections) < 2:
                v = random.choice([n for n in range(nodes) if n != node and n != source and n != sink and n not in connections])
                capacity = random.randint(5, 20)
                if not G.has_edge(node, v):
                    G.add_edge(node, v, capacity=capacity, flow=0)
                    G.add_edge(v, node, capacity=0, flow=0)
                    connections.append(v)

    return G

def create_random_network_with_constraints(nodes, edges, source, sink):
    G = nx.DiGraph()

    # Create direct connections from source to intermediate nodes, and from intermediate nodes to sink
    for i in range(1, nodes - 1):
        G.add_edge(source, i, capacity=random.randint(10, 20), flow=0)
        G.add_edge(i, sink, capacity=random.randint(10, 20), flow=0)

    # Add additional intermediate connections
    for i in range(1, nodes - 1):
        for j in range(1, nodes - 1):
            if i != j and not G.has_edge(i, j):
                G.add_edge(i, j, capacity=random.randint(5, 15), flow=0)

    # Add reverse edges for all existing edges with 0 initial flow
    for u, v in list(G.edges()):
        if not G.has_edge(v, u):
            G.add_edge(v, u, capacity=0, flow=0)

    # Add extra random edges until reaching the desired edge count
    while len(G.edges()) < edges:
        u = random.choice(range(nodes))
        v = random.choice(range(nodes))
        if u != v and not G.has_edge(u, v) and not (u == sink or v == source):
            G.add_edge(u, v, capacity=random.randint(5, 15), flow=0)
            if not G.has_edge(v, u):
                G.add_edge(v, u, capacity=0, flow=0)  # Reverse edge

    return G


def print_residual_graph(G):
    for u, v, data in G.edges(data=True):
        residual_capacity = data['capacity'] - data['flow']
        print(f"Residual capacity from {u} to {v}: {residual_capacity}")


def update(frame, G, pos, ax, steps):
    ax.clear()
    ax.set_title(f"Step {frame}")

    # Get the flow data for this step
    current_flows = steps[frame]

    # Highlight the nodes that are part of the flow at this step
    visited_nodes = set()
    for (u, v), flow in current_flows.items():
        if flow > 0:
            visited_nodes.add(u)
            visited_nodes.add(v)

    # Set node colors based on visit status
    node_colors = []
    for node in G.nodes:
        if node in visited_nodes:
            node_colors.append('orange')  # Color for visited nodes
        else:
            node_colors.append('lightblue')  # Color for unvisited nodes

    # Draw the graph
    nodes = nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors)
    edges = nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray')
    labels = nx.draw_networkx_labels(G, pos, ax=ax)

    # Draw the flow on edges
    edge_labels = {(u, v): f"{flow}" for (u, v), flow in current_flows.items() if flow > 0}
    edge_texts = nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

    # Return the artists that were drawn
    artists = [nodes] + list(edges) + list(labels.values()) + list(edge_texts.values())
    return artists


def main():
    random.seed(42)

    nodes = 6
    edges = 15
    source = 0
    sink = nodes - 1

    G = create_random_network_with_constraints(nodes, edges, source, sink)
    pos = nx.spring_layout(G)

    max_flow, steps = ford_fulkerson(G, source, sink)
    print(f"Maximum Flow: {max_flow}")
    print(f"Total steps recorded: {len(steps)}")

    for i, step in enumerate(steps):
        print(f"Step {i}: {step}")

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update, frames=len(steps), fargs=(G, pos, ax, steps), repeat=False)
    ani.save('ford_fulkerson_animation.gif', writer='pillow')
    plt.show()

if __name__ == "__main__":
    main()
