import unittest
from unittest_data_provider import data_provider
import random
from graph_adjacency_matrix import Graph

class GraphTest(unittest.TestCase):
    def buildGraphFromAdjacencyList(graph, n):
        g = Graph(n)
        for vertex, neighbors in graph.items():
            for neighbor in neighbors:
                g.addEdge(vertex, neighbor)
        return g

    def test_all(self):
        data = [
            GraphTest.buildGraphFromAdjacencyList({0:[1,2], 1:[3], 2:[4], 3:[4]}, 5),
            GraphTest.buildGraphFromAdjacencyList({
                0:[1,2,3,4,5,6],
                1:[7],
                7:[8],
                8:[9,10,11,12,13]
            }, 14)
        ]

        for g in data:
            print("Graph", g)
            for s in [0,1,2,3,4]:
                bfs, dfs = g.BFS(s), g.DFS(s)
                print("BFS from %d: %s" % (s, str(bfs)))
                print("DFS from %d: %s" % (s, str(dfs)))


