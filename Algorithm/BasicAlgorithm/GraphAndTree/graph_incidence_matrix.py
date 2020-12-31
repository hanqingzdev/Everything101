class Graph:
    def __init__(self, n):
        self.graph = [[] for i in range(n)]
    def __str__(self):
        return str(self.graph)

    def addEdge(self, vertex1, vertex2, weight=1):
        for vertex in range(len(self.graph)):
            adjVal = weight if vertex in [vertex1, vertex2] else 0
            adjRow = self.graph[vertex]
            adjRow.append(adjVal)

    def _findTheOtherV(self, vertex, edge):
        for v in range(len(self.graph)):
            adjs = self.graph[v]
            if adjs[edge] > 0 and v != vertex:
                return v
        return None # should never happen

    def BFS(self, start):
        visited = set()
        toVisit = [] # Queue
        output = []

        toVisit.append(start)

        while len(toVisit) > 0:
            vertex = toVisit.pop(0)

            if vertex in visited:
                continue

            output.append(vertex)
            visited.add(vertex)

            adjs = self.graph[vertex]
            for edge in range(len(adjs)):
                if edge > 0:
                    theOtherV = self._findTheOtherV(vertex, edge)
                    toVisit.append(theOtherV)

        return output

    def DFS(self, start):
        visited = set()
        output = []

        def dfs(vertex):
            if vertex in visited:
                return
            visited.add(vertex)
            output.append(vertex)

            adjs = self.graph[vertex]
            for edge in range(len(adjs)):
                theOtherV = self._findTheOtherV(vertex, edge)
                dfs(theOtherV)

        dfs(start)
        return output
