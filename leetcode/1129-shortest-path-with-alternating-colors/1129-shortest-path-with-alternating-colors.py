from collections import deque, defaultdict

class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
      
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u, v in redEdges:
            red_graph[u].append(v)

        for u, v in blueEdges:
            blue_graph[u].append(v)

        queue = deque([(0, -1, 0)]) 

        visited = set([(0, -1)])

        res = [-1] * n

        while queue:
            node, color, dist = queue.popleft()

            if res[node] == -1:
                res[node] = dist

            if color != 0:
                for nei in red_graph[node]:
                    if (nei, 0) not in visited:
                        visited.add((nei, 0))
                        queue.append((nei, 0, dist + 1))

            if color != 1:
                for nei in blue_graph[node]:
                    if (nei, 1) not in visited:
                        visited.add((nei, 1))
                        queue.append((nei, 1, dist + 1))

        return res