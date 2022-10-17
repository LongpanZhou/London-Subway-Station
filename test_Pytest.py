from Pytest_Main import route
import pytest

out_cost = []
out_route = []

for i in range(1, 6):
    with open(f'./_samples/case{i}.out') as file:
        data = file.readline().split("-")
        out_cost.append(int(data[0]))
        tmp_list = []
        for i in data[1].strip("[] ").split(","):
            tmp_list.append(int(i))
        out_route.append(tmp_list)


def test_case_1():
    with open(f'./_samples/case1.in') as file:
        (cost, path) = route(file)
        assert cost == out_cost[0]
        assert path == out_route[0]


def test_case_2():
    with open(f'./_samples/case2.in') as file:
        (cost, path) = route(file)
        assert cost == out_cost[1]
        assert path == out_route[1]


def test_case_3():
    with open(f'./_samples/case3.in') as file:
        (cost, path) = route(file)
        assert cost == out_cost[2]
        assert path == out_route[2]


def test_case_4():
    with open(f'./_samples/case4.in') as file:
        (cost, path) = route(file)
        assert cost == out_cost[3]
        assert path == out_route[3]


def test_case_5():
    with open(f'./_samples/case5.in') as file:
        (cost, path) = route(file)
        assert cost == out_cost[4]
        assert path == out_route[4]
