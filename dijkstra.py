import networkx as nx

def dijkstra_path(graph,start,goal):
    return nx.dijkstra_path(graph,start,goal,weight="weight")