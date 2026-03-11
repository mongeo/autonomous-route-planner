import networkx as nx

def heuristic(a,b):
    return 1

def astar_path(graph,start,goal):
    return nx.astar_path(graph,start,goal,heuristic=heuristic,weight="weight")