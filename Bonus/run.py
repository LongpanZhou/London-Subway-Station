from RandomGraphGenerator import rdg

rdg_1 = rdg(2, [1, 1], 1, 1)
print(rdg_1.generate().getGraph())

rdg_2 = rdg(10, [2, 3, 4, 5, 2, 4, 2, 3, 5, 1], 3, 3)
print(rdg_2.generate().getGraph())
