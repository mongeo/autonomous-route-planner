from graph import create_sample_graph
from traffic_simulation import apply_traffic
from astar import astar_path
from dijkstra import dijkstra_path
from visualizer import draw_graph

def main():

    graph = create_sample_graph()

    apply_traffic(graph)

    start = "A"
    goal = "F"

    path_astar = astar_path(graph,start,goal)
    path_dijkstra = dijkstra_path(graph,start,goal)

    print("A* Path:",path_astar)
    print("Dijkstra Path:",path_dijkstra)

    draw_graph(graph,path_astar)

if __name__ == "__main__":
    main()