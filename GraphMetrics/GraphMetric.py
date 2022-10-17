from abc import abstractmethod
from Graph import Graph


class GraphMetric(Graph):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getMetric(self):
        ...
