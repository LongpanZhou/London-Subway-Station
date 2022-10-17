from Strategy.Algorithms import Algorithms
import sys


class Dijkstra(Algorithms):
    def __init__(self):
        pass

    def runalgorithm(self, g, start, end):
        numnodesvisited = 0
        linesused = 0
        numofcomparisons = 0
        numofiterations = 0

        #print("Running Dijksra's algorithm")
        inf = sys.maxsize
        distance = {}
        pred = {}
        unvisited = g.graph.copy()
        path = []
        count = 0
        output = {
            "weight": 0,
            "path": 0,
            "numnodesvisited": 0,
            "numofcomparisons": 0,
            "numofiterations": 0}

        for i in g.graph:
            distance[i] = inf
        distance[start] = 0

        while unvisited:
            count += 1
            min_dis_node = None
            for node in unvisited:
                numnodesvisited += 1
                if min_dis_node is None:
                    min_dis_node = node
                elif distance[node] < distance[min_dis_node]:
                    numofcomparisons += 1
                    min_dis_node = node
                numofiterations += 1

            for m, line, weight in g.graph[min_dis_node]:
                if distance[min_dis_node] + weight < distance[m]:
                    numofcomparisons += 1
                    distance[m] = distance[min_dis_node] + weight
                    pred[m] = min_dis_node
            unvisited.pop(min_dis_node)

            numofiterations += 1

        current = end

        while current != start:
            try:
                path.insert(0, current)
                current = pred[current]
            except BaseException:
                break

        path.insert(0, start)

        if distance[end] != inf:
            #print('Time Cost: {}'.format(distance[end]))
            output["weight"] = (distance[end])
            #print('Path found: {}'.format(path))
            output["path"] = (path)

            output["numnodesvisited"] = (numnodesvisited)
            output["numofiterations"] = (numofiterations)
            output["numofcomparisons"] = (numofcomparisons)
        else:
            print('Path does not exist!')
            return
        return output
