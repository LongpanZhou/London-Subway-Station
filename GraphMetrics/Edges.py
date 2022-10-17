from GraphMetrics.GraphMetric import GraphMetric


class Edges(GraphMetric):
    def __init__(self, thegraph):
        super().__init__()
        self.graph = thegraph.getGraph()

    def getMetric(self):
        numedges = 0
        for i in (self.graph):
            numedges += len(self.graph[i])

        return numedges // 2
