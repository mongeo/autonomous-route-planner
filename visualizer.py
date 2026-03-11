import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph,path=None):

    pos = nx.spring_layout(graph)

    nx.draw(graph,pos,with_labels=True,node_size=1500)

    labels = nx.get_edge_attributes(graph,"weight")
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)

    if path:
        edges = list(zip(path,path[1:]))
        nx.draw_networkx_edges(graph,pos,edgelist=edges,width=4)

    plt.title("Autonomous Route Planner")
    plt.show()