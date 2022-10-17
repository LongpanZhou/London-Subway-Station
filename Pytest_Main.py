from GraphMetrics.ConnectedComponents import ConnectedComponents
from Graph import Graph
from GraphMetrics.Nodes import Nodes
from GraphMetrics.Edges import Edges
from Factory.ExtractionSpawner import ExtractionSpawner
from Itinerary import Itinerary

graph = Graph()
Spawner = ExtractionSpawner()
thegraph = Spawner.spawn("type1", graph)
thegraph.createGraph()


def route(input_stream):
    start, end = input_stream.readline().strip().split(" ")
    itiner = Itinerary(int(start), int(end), graph)
    return (itiner.traveltime_astar, itiner.route_astar)
