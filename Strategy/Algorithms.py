from abc import ABC, abstractmethod


class Algorithms(ABC):
    def __init__(self, graph):
        self.graph = graph

    def setStrat(self, algo):
        self.algo = algo

    def runalgorithm(self, start, end):
        if (self.algo == "None"):
            print("no algorithm selected")
        else:
            return self.algo.runalgorithm(self.graph, start, end)

    def runtspalgorithm(self, stationstovisit):
        if (self.algo == "None"):
            print("no algorithm selected")
        else:
            return self.algo.runtspalgorithm(self.graph, stationstovisit)
