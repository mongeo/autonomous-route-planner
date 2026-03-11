import networkx as nx

def create_sample_graph():
    G = nx.Graph()

    edges = [
        ("A","B",4),
        ("A","C",2),
        ("B","C",1),
        ("B","D",5),
        ("C","D",8),
        ("C","E",10),
        ("D","E",2),
        ("D","F",6),
        ("E","F",3)
    ]

    for u,v,w in edges:
        G.add_edge(u,v,weight=w)

    return G