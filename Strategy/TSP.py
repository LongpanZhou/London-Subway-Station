from Strategy.Algorithms import Algorithms
from Strategy.Dijkstra import Dijkstra
from sys import maxsize
from itertools import permutations


class TSP(Algorithms):

    def __init__(self):
        pass

    # implementation of traveling Salesman Problem
    def runtspalgorithm(self, g, stationstovisit):

        algorithmtouse = Algorithms(g)
        algorithmtouse.setStrat(Dijkstra())

        permutationsofpath = list(
            permutations(
                stationstovisit,
                len(stationstovisit)))
        shortestdistance = maxsize
        shortestpath = []
        notpossible = False

        for path in permutationsofpath:

            notpossible = False

            current_pathweight = 0
            current_path = []
            stationsvisited = []
            stationsvisited.append(path[0])
            current_path.append(path[0])

            for i in range(len(path) - 1):
                if path[i + 1] in stationsvisited:
                    continue

                curr_shortestpath = algorithmtouse.runalgorithm(
                    path[i], path[i + 1])

                current_pathweight += curr_shortestpath["weight"]

                for j in range(1, len(curr_shortestpath["path"])):

                    if curr_shortestpath["path"][j] in stationsvisited:
                        notpossible = True
                        break
                    stationsvisited.append(curr_shortestpath["path"][j])
                    current_path.append(curr_shortestpath["path"][j])

            if current_pathweight < shortestdistance and notpossible == False:
                shortestdistance = current_pathweight
                shortestpath = current_path

        if len(shortestpath) == 0:
            print("no possible path")
            return

        print(
            "The most efficient path for stations",
            stationstovisit,
            "is:",
            shortestpath,
            "with a travel time of:",
            shortestdistance)
        return
