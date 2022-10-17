from GraphMetrics.GraphMetric import GraphMetric
from collections import deque


class ConnectedComponents(GraphMetric):
    def __init__(self, thegraph):
        super().__init__()
        self.graph = thegraph.getDirectedGraph()

    def getMetric(self):

        seen = set()
        output = []

        for root in self.graph.keys():
            if root not in seen:
                seen.add(root)
                component = []
                queue = deque([root])

                while queue:
                    node = queue.popleft()
                    component.append(node)
                    for neighbor, line, weight in self.graph[node]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)
                output.append(component)

        return output
