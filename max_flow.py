# from https://www.geeksforgeeks.org/minimum-cut-in-a-directed-graph/
from copy import deepcopy


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.org_graph = deepcopy(graph)
        self.ROW = len(graph)
        self.COL = len(graph[0])
        self.res = list()

    def BFS(self, s, t, parent):
        visited = [False] * self.ROW
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def minCut(self, source, sink):

        parent = [-1] * self.ROW
        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and self.org_graph[i][j] > 0:
                    self.res.append([i, j])
        return self.res
