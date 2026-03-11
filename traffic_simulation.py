import random

def apply_traffic(graph):
    for u,v,data in graph.edges(data=True):
        traffic = random.uniform(1.0,2.5)
        data["weight"] *= traffic