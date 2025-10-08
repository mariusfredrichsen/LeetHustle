class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        E = dict()
        w = dict()
        for i in range(1, n+1):
            E[i] = set()
        for r in roads:
            E[r[0]].add(r[1])
            E[r[1]].add(r[0])
            w[(r[0],r[1])] = r[2]
            w[(r[1],r[0])] = r[2]

        def bfs(E):
            queue = [1]
            visited = set()
            min_val = float('inf')
            V = set()
            V.add(1)
            
            while queue:
                v = queue.pop(0)
                for u in E[v]:
                    if u not in visited:
                        visited.add(u)
                        queue.append(u)
                        V.add(u)
            return V
        V = bfs(E)
        min_val = float('inf')
        for v in E:
            for u in E[v]:
                if v in V and u in V:
                    if min_val > w[(v, u)]:
                        min_val = w[(v,u)]
        
        return min_val