class Graph:
    def __init__(self, n):
        self.graph = [[0] * n for i in range(n)]
    def __str__(self):
        return str(self.graph)

    def addEdge(self, vertex1, vertex2, weight=1):
        self.graph[vertex1][vertex2] = weight
        self.graph[vertex2][vertex1] = weight

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

            edges = self.graph[vertex]
            for neighbor in range(len(self.graph)):
                if edges[neighbor] > 0:
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

            edges = self.graph[vertex]
            for neighbor in range(len(self.graph)):
                if edges[neighbor] > 0:
                    dfs(neighbor)

        dfs(start)
        return output
