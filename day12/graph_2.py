# G = (V, E)
from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges"])

nodes = ["A", "B", "C", "D"]
edges = [
    ("A", "B"),
    ("A", "B"),
    ("A", "C"),
    ("A", "C"),
    ("A", "D"),
    ("B", "D"),
    ("C", "D")
]

nodes2 = range(4)
edges2 = [
    (0, 1),
    (0, 1),
    (0, 2),
    (0, 2),
    (0, 3),
    (1, 3),
    (2, 3)
]

G = Graph(nodes, edges)
NG = Graph(nodes2, edges2)

def adjacency_dict(graph):
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        adj[node2].append(node1)
    return adj

# adjacency_dict(G) {'A': ['B', 'B', 'C', 'C', 'D'], 'B': ['A', 'A', 'D'], 'C': ['A', 'A', 'D'], 'D': ['A', 'B', 'C']}

def adjacency_matrix(graph):
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] += 1
        adj[node2][node1] += 1
    return adj

Bridges = [
    "AaB",
    "AbB",
    "AcC",
    "AdC",
    "AeD",
    "BfD",
    "CgD"
]

def get_walks_starting_from(area, bridges=Bridges):
    walks = []

    def make_walks(area, walked=None, bridges_crossed=None):
        walked = walked or area
        bridges_crossed = bridges_crossed or ()
        available_bridges = [
            bridges
            for bridge in bridges
            if area in bridge and bridge not in bridges_crossed
        ]

        if not available_bridges:
            walks.append(walked)

        for bridge in available_bridges:
            crossing = bridge[1:] if bridge[0] == area else bridge[1::-1]
            make_walks(
                area=crossing[-1],
                walked=walked + crossing,
                bridges_crossed=(bridge, *bridges_crossed)
            )

        make_walks(area)
        return walks

if __name__ == '__main__':
    walks_starting_from = {area: get_walks_starting_from(area) for area in "ABCD"}
    num_total_walks = sum(len(walks) for walks in walks_starting_from.values())
    print(num_total_walks)