import random
from Graph import Graph
from Factory.ExtractionSpawner import ExtractionSpawner
from Strategy.Algorithms import Algorithms
from Strategy.AStar import AStar
from Strategy.Dijkstra import Dijkstra
import time
import matplotlib.pyplot as plt


def main():
    """Running the complete benchmark"""

    graph = Graph()
    Spawner = ExtractionSpawner()
    thegraph = Spawner.spawn("type1", graph)
    thegraph.createGraph()

    listofstations = []
    for key in graph.graph:
        listofstations.append(int(key))

    dataset = {
        "10": [],
        "50": [],
        "100": [],
        "250": [],
        "500": [],
        "1000": []
    }

    for key in dataset:
        for i in range(int(key)):
            dataset[key].append(gen_stations(listofstations))

    # create algorithm object for this graph
    algorithm = Algorithms(graph)

    # set algorithm to dijkstra and calculate path
    algorithm.setStrat(Dijkstra())
    print("Running Benchmark on Dataset with Dijkstra")
    benchdata_dijkstra = multi_pathfind(algorithm, dataset)

    print("Number of Nodes Visited:")
    print(benchdata_dijkstra[0])

    print("Number of Comparisons:")
    print(benchdata_dijkstra[1])

    print("Number of Iterations:")
    print(benchdata_dijkstra[2])

    print("Execution Times:")
    print(benchdata_dijkstra[3])

    print("Running Benchmark on Dataset with AStar")
    algorithm.setStrat(AStar())
    benchdata_astar = multi_pathfind(algorithm, dataset)

    print("Number of Nodes Visited:")
    print(benchdata_astar[0])

    print("Number of Comparisons:")
    print(benchdata_astar[1])

    print("Number of Iterations:")
    print(benchdata_astar[2])

    print("Execution Times:")
    print(benchdata_astar[3])

    plotstuff(benchdata_astar, benchdata_dijkstra)


def multi_pathfind(algorithmtouse: Algorithms, dataset):
    resultnumnodes = {
        "10": 0,
        "50": 0,
        "100": 0,
        "250": 0,
        "500": 0,
        "1000": 0
    }
    resultcomparisons = {
        "10": 0,
        "50": 0,
        "100": 0,
        "250": 0,
        "500": 0,
        "1000": 0
    }
    resultiterations = {
        "10": 0,
        "50": 0,
        "100": 0,
        "250": 0,
        "500": 0,
        "1000": 0
    }
    resultexecutiontimes = {
        "10": 0,
        "50": 0,
        "100": 0,
        "250": 0,
        "500": 0,
        "1000": 0
    }

    for k in dataset:
        for i in range(int(k)):
            timestart = time.time()
            data = algorithmtouse.runalgorithm(
                dataset[k][i][0], dataset[k][i][1])
            resultnumnodes[k] += data["numnodesvisited"]
            resultcomparisons[k] += data["numofcomparisons"]
            resultiterations[k] += data["numofiterations"]
            resultexecutiontimes[k] += time.time() - timestart

    return resultnumnodes, resultcomparisons, resultiterations, resultexecutiontimes

# return two random stations in range of all the stations


def gen_stations(stationlist):
    n = [random.choice(stationlist), random.choice(stationlist)]
    return n


def plotstuff(astar_data, dijkstra_data):
    fig, ax = plt.subplots(nrows=2, ncols=2)

    ax[0, 0].plot(astar_data[0].keys(), astar_data[0].values(),
                  color='r', label='A*')
    ax[0, 0].plot(dijkstra_data[0].keys(),
                  dijkstra_data[0].values(), color='b', label='Dijkstra')
    ax[0, 0].set_xlabel('array size')
    ax[0, 0].set_ylabel('Nodes Visited')
    ax[0, 0].title.set_text("Nodes Visited Per Number of Runs")

    ax[0, 1].plot(astar_data[1].keys(), astar_data[1].values(),
                  color='r', label='A*')
    ax[0, 1].plot(dijkstra_data[1].keys(),
                  dijkstra_data[1].values(), color='b', label='Dijkstra')
    ax[0, 1].set_xlabel('array size')
    ax[0, 1].set_ylabel('Number of Comparisons')
    ax[0, 1].title.set_text("Number of Comparisons Per Number of Runs")

    ax[1, 0].plot(astar_data[2].keys(), astar_data[2].values(),
                  color='r', label='A*')
    ax[1, 0].plot(dijkstra_data[2].keys(),
                  dijkstra_data[2].values(), color='b', label='Dijkstra')
    ax[1, 0].set_xlabel('array size')
    ax[1, 0].set_ylabel('Number of Iterations')
    ax[1, 0].title.set_text("Number of Iterations Per Number of Runs")

    ax[1, 1].plot(astar_data[3].keys(), astar_data[3].values(),
                  color='r', label='A*')
    ax[1, 1].plot(dijkstra_data[3].keys(),
                  dijkstra_data[3].values(), color='b', label='Dijkstra')
    ax[1, 1].set_xlabel('array size')
    ax[1, 1].set_ylabel('Execution Time')
    ax[1, 1].title.set_text("Execution Time Per Number of Runs")
    plt.show()


main()
