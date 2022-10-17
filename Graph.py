class Graph():
    def __init__(self):
        self.graph = {}
        self.visited = []
        self.gps = {}
        self.directed = {}

    def addNode(self, v):
        if int(v) not in self.graph:
            self.graph[int(v)] = []
            self.directed[int(v)] = []

    def addEdge(self, start, end, line, time):
        if start not in self.graph:
            print("Vertex ", start, " does not exist.")
        elif end not in self.graph:
            print("Vertex ", end, " does not exist.")
        else:
            self.graph[start].append([end, line, time])
            self.graph[end].append([start, line, time])
            self.directed[start].append([end, line, time])

    def addGPS(self, id, lat, lot):
        self.gps[id] = []
        self.gps[id].append([lat, lot])

    def getGraph(self):
        return self.graph

    def getDirectedGraph(self):
        return self.directed
