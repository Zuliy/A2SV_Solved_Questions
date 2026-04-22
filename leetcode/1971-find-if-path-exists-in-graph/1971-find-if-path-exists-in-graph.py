class Solution(object):
    def validPath(self, n, edges, source, destination):
      
        visited = set()
        graph = defaultdict(list)
        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node ):

            #base case
            if node == destination:
                return True
            visited.add(node)

            #path
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True

            return False
        return dfs(source)
        