from Strategy.Algorithms import Algorithms
from Strategy.AStar import AStar
from Strategy.Dijkstra import Dijkstra


class Itinerary():
    def __init__(self, start, end, graph):
        self.graph = graph.getGraph()
        algorithm = Algorithms(graph)
        algorithm.setStrat(AStar())
        astar_stuff = algorithm.runalgorithm(start, end)

        self.route_astar = astar_stuff["path"]

        algorithm.setStrat(Dijkstra())
        dijkstra_stuff = algorithm.runalgorithm(start, end)

        self.route_dijkstra = dijkstra_stuff["path"]

        self.start = start
        self.end = end
        self.traveltime_astar = astar_stuff["weight"]
        self.traveltime_dijkstra = dijkstra_stuff["weight"]

        # calculate how many lines are switched in the paths

    def getItinerary(self):
        print(
            "AStar Path for Station ",
            self.start,
            "to Station ",
            self.end,
            "\n")
        print(self.route_astar)
        print("\nTravel Time: ", self.traveltime_astar)
        #print("\nNumber of Train Switches: " + self.numofswitches_astar)
        print(
            "\nDijkstra Path for Station ",
            self.start,
            "to Station ",
            self.end,
            "\n")
        print(self.route_dijkstra)
        print("\nTravel Time: ", self.traveltime_dijkstra)
        #print("\nNumber of Train Switches: " + self.numofswitches_dijkstra)

        return
