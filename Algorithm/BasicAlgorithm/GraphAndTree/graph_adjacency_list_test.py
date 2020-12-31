import unittest
from unittest_data_provider import data_provider
import random
from graph_adjacency_list import Graph

class GraphTest(unittest.TestCase):
    def buildGraphFromAdjacencyList(graph):
        g = Graph()
        for vertex, neighbors in graph.items():
            for neighbor in neighbors:
                g.addEdge(vertex, neighbor)

        return g

    def test_all(self):
        data = [
            GraphTest.buildGraphFromAdjacencyList({0:[1,2], 1:[3], 2:[4], 3:[4]}),
            GraphTest.buildGraphFromAdjacencyList({
                0:[1,2,3,4,5,6],
                1:[7],
                7:[8],
                8:[9,10,11,12,13]
            })
        ]

        for g in data:
            print("Graph", g)
            for s in [0,1,2,3,4]:
                bfs, dfs = g.BFS(s), g.DFS(s)
                print("BFS from %d: %s" % (s, str(bfs)))
                print("DFS from %d: %s" % (s, str(dfs)))


    def test_dijkstra(self):
        # Example from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        g = Graph()
        g.addEdge(1, 2, 7)
        g.addEdge(1, 3, 9)
        g.addEdge(2, 3, 10)
        g.addEdge(1, 6, 14)
        g.addEdge(2, 4, 15)
        g.addEdge(3, 6, 2)
        g.addEdge(3, 4, 11)
        g.addEdge(4, 5, 6)
        g.addEdge(5, 6, 9)

        dist = g.bestPath_Dijkstra(1, 5)
        self.assertEqual(20, dist)

if __name__ == '__main__':
    unittest.main()
