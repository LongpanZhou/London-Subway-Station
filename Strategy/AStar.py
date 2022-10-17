from Strategy.Algorithms import Algorithms


class AStar(Algorithms):
    def __init__(self):
        pass

    def heuristic(self, graph, node):
        return (graph.gps[node][0][0]**2 + graph.gps[node][0][1]**2)**0.5

    def runalgorithm(self, g, start, end):
        #print("Running AStar's algorithm")

        numnodesvisited = 0
        linesused = 0
        numofcomparisons = 0
        numofiterations = 0

        graph_nodes = g.graph
        open_set = set()
        open_set.add(start)

        output = {
            "weight": 0,
            "path": 0,
            "numnodesvisited": 0,
            "numofcomparisons": 0,
            "numofiterations": 0}
        closed_set = set()
        distance = {}
        parents = {}
        distance[start] = 0
        parents[start] = start
        while len(open_set) > 0:
            n = None
            for v in open_set:
                numnodesvisited += 1
                if n is None or distance[v] + self.heuristic(
                        g, v) < distance[n] + self.heuristic(g, n):
                    numofcomparisons += 1
                    n = v
                numofiterations += 1
            if n == end or graph_nodes[n] is None:
                pass
            else:
                for (m, line, weight) in graph_nodes[n]:
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        distance[m] = distance[n] + weight
                    else:
                        if distance[m] > distance[n] + weight:
                            numofcomparisons += 1
                            distance[m] = distance[n] + weight
                            parents[m] = n
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
            if n is None:
                print('Path does not exist!')
                return None

            if n == end:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start)
                path.reverse()
                #print('Time Cost: {}'.format(distance[end]))
                output["weight"] = (distance[end])
                #print('Path found: {}'.format(path))
                output["path"] = (path)
                output["numnodesvisited"] = (numnodesvisited)
                output["numofiterations"] = (numofiterations)
                output["numofcomparisons"] = (numofcomparisons)
                return output
            open_set.remove(n)
            closed_set.add(n)

            numofiterations += 1
        print('Path does not exist!')
        return None
