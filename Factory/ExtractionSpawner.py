from Factory.GraphBuilder import GraphBuilder
from Factory.Extraction1 import Extraction1


class ExtractionSpawner(GraphBuilder):
    def __init__(self):
        super().__init__()

    def spawn(self, type, graph):
        if type == "type1":
            return Extraction1(graph)
        # elif self.type == "type2":
        #    return Extraction2(self.type)
        else:
            return None
