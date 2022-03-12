# Задание №1

import collections


class Solution:

    def make_connected(self, n, connections):

        data = list(range(n))

        def find(x):

            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):

            data[data[x]] = data[y]

        extra_edges = 0
        for u, v in connections:
            pu, pv = find(u), find(v)
            if pu != pv:
                union(u, v)
            else:
                extra_edges += 1

        components = len(set(find(u) for u in range(n)))
        if extra_edges < components - 1:
            return -1
        else:
            return components - 1

    def make_connected_sol2(self, n, connections):

        if len(connections) < n - 1:
            return -1

        data = list(range(n))

        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            data[data[x]] = data[y]

        for u, v in connections:
            if find(u) != find(v):
                union(u, v)

        return len(set(find(u) for u in range(n))) - 1

    def make_connected_sol3(self, n, connections):

        if len(connections) < n - 1:
            return -1

        graph, visited = collections.defaultdict(set), set()
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(u):
            if u in visited:
                return 0
            visited.add(u)
            for v in graph[u]:
                dfs(v)
            return 1

        return sum(dfs(u) for u in range(n)) - 1

sol = Solution()
print(sol.make_connected_sol3(4, [[0,1],[0,2],[1,2]]))
print(sol.make_connected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(sol.make_connected_sol2(6, [[0,1],[0,2],[0,3],[1,2]]))