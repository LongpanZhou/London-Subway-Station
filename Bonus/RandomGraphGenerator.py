import random

from Graph import Graph


class rdg:

    def __init__(self, num_nodes, num_degrees, num_lines, max_time):
        if num_nodes == len(num_degrees) and num_lines > 0 and max_time > 0:
            self.num_nodes = num_nodes
            self.num_degrees = num_degrees
            self.num_lines = num_lines
            self.max_time = max_time
        else:
            self.num_nodes = 0
            self.num_degrees = 0
            self.num_lines = 0
            self.max_time = 0
            print("Number of Edges given does not match the length of num_degrees list")

    def generate(self):
        graph = Graph()

        def random_exclude(exclude):
            r = exclude
            while r == exclude:
                r = random.randint(1, self.num_nodes)
            return r

        for i in range(self.num_nodes):
            print(f"adding{i + 1}")
            graph.addNode(i + 1)
            for j in range(self.num_degrees[i]):
                graph.addEdge(i + 1, random_exclude(i + 1), random.randint(1, self.num_lines), random.randint(1, self.max_time))

        return graph
