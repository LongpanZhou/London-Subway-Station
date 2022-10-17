from abc import ABC, abstractmethod


class Extractors(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def createGraph(self):
        pass
