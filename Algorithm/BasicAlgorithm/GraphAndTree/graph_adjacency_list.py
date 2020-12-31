from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex1, vertex2, weight=1):
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))

    def BFS(self, start):
        visited = set()
        toVisit = [] # Queue
        output = []

        toVisit.append(start)

        while len(toVisit) > 0:
            vertex = toVisit.pop(0)
            if vertex in visited:
                continue

            visited.add(vertex)
            output.append(vertex)

            for neighbor in self.graph[vertex]:
                toVisit.append(neighbor)

        return output

    def DFS(self, start):
        visited = set()
        output = []

        def dfs(vertex):
            if vertex in visited:
                return
            visited.add(vertex)
            output.append(vertex)

            for neighbor in self.graph[vertex]:
                dfs(neighbor)

        dfs(start)
        return output

    def bestPath_Dijkstra(self, v1, v2):
        dist = {v1: 0}

        visited = set()
        toVisit = [v1]

        while len(toVisit) > 0:
            v = toVisit.pop(0)
            if v in visited:
                continue

            vDist = dist[v]
            visited.add(v)

            for neighbor, weight in self.graph[v]:
                newDist = vDist + weight
                dist[neighbor] = min(dist.get(neighbor) or newDist, newDist)
                toVisit.append(neighbor)

        return dist.get(v2)

