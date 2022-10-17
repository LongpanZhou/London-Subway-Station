from abc import abstractmethod
from Graph import Graph


class GraphBuilder(Graph):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def spawn():
        pass
    '''
    @abstractmethod
    def createGraph(self):
        ...'''
