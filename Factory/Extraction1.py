from Factory.Extractors import Extractors


class Extraction1(Extractors):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph

    def createGraph(self):
        with open('./_dataset/london.stations.csv', 'r') as f:
            next(f)
            for j in f:
                self.graph.addNode(j.split(',')[0])
        f.close()

        with open('./_dataset/london.connections.csv', 'r') as f:
            next(f)
            for j in f:
                v1 = int(j.split(',')[0])
                v2 = int(j.split(',')[1])
                line = int(j.split(',')[2])
                time = int((j.split(',')[3]).strip())
                self.graph.addEdge(v1, v2, line, time)

        f.close()

        with open('./_dataset/london.stations.csv') as f:
            next(f)
            for j in f:
                id = int(j.split(',')[0])
                lat = float(j.split(',')[1])
                lot = float(j.split(',')[2])
                self.graph.addGPS(id, lat, lot)

        f.close()
        return self.graph
