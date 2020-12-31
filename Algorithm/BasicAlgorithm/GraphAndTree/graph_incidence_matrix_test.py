import unittest
from unittest_data_provider import data_provider
import random
import networkx as nx
from networkx.generators.random_graphs import gnm_random_graph as random_graph
from networkx.algorithms.traversal.depth_first_search import dfs_edges
from networkx.algorithms.traversal.breadth_first_search import bfs_edges

import matplotlib.pyplot as plt


from graph_incidence_matrix import Graph

class GraphTest(unittest.TestCase):
    def buildGraphFromNXGraph(nxGraph):
        g = Graph(nxGraph.number_of_nodes())
        for v1, v2 in nxGraph.edges():
            g.addEdge(v1, v2)
        return g

    def expectedOutput(nxG, source, traverseFn):
        edges = list(traverseFn(nxG, source))
        output = [source]
        output.extend([v2 for (v1, v2) in edges])
        return output

    def test_all(self):
        nxGraphs = [
            nx.path_graph(5),
            random_graph(4,5),
            random_graph(4,6),
            random_graph(5,5)
        ]
        data = [ (GraphTest.buildGraphFromNXGraph(nxGraph), nxGraph) for nxGraph in nxGraphs ]

        for g, nxG in data:
            #print("Graph", g)
            #plt.subplot(121)
            #nx.draw(nxG)
            #plt.show()
            print(nxG.edges())
            for s in [0,1,2,3]:
                bfs, dfs = g.BFS(s), g.DFS(s)
                nxBFS = GraphTest.expectedOutput(nxG, s, bfs_edges)
                nxDFS = GraphTest.expectedOutput(nxG, s, dfs_edges)
                print("   BFS from %d: %s" % (s, str(bfs)))
                print("NX BFS from %d: %s" % (s, str(nxBFS)))
                print("   DFS from %d: %s" % (s, str(dfs)))
                print("NX DFS from %d: %s" % (s, str(nxDFS)))


