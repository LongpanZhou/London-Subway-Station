from GraphMetrics.GraphMetric import GraphMetric


class Nodes(GraphMetric):
    def __init__(self, thegraph):
        super().__init__()
        self.graph = thegraph.getGraph()

    def getMetric(self):
        return len(self.graph)
