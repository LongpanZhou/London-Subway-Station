from GraphMetrics.ConnectedComponents import ConnectedComponents
from Graph import Graph
from GraphMetrics.Nodes import Nodes
from GraphMetrics.Edges import Edges
from Factory.ExtractionSpawner import ExtractionSpawner
from Itinerary import Itinerary
from Strategy.Algorithms import Algorithms
from Strategy.AStar import AStar
from Strategy.Dijkstra import Dijkstra
from Strategy.TSP import TSP


def run():

    # create the graph
    graph = Graph()
    Spawner = ExtractionSpawner()
    thegraph = Spawner.spawn("type1", graph)
    thegraph.createGraph()

    # print graph for visibility
    # print(graph.graph)

    # calculate and print metrics
    nodes = Nodes(graph)
    edges = Edges(graph)
    connectedcomponents = ConnectedComponents(graph)
    print("\n\nNumber of nodes: ", nodes.getMetric())
    print("Number of edges: ", edges.getMetric(), "\n")
    # print(connectedcomponents.getMetric())

    # create algorithm object for this graph
    algorithm = Algorithms(graph)

    # set algorithm to dijkstra and calculate path
    # algorithm.setStrat(Dijkstra())
    # print(algorithm.runalgorithm(11,13))

    # set algorithm to astar and calculate path
    # algorithm.setStrat(AStar())
    # print(algorithm.runalgorithm(11,13))

    # create itinerary object between two stations and return best path from
    # either A* or Dijkstra
    itin1 = Itinerary(11, 300, graph)
    itin1.getItinerary()

    # set algorithm to tsp for most efficient path containing certain stations
    algorithm.setStrat(TSP())
    algorithm.runtspalgorithm([20,21,23,25])


run()
