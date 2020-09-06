class Solution:

    def __init__(self):
        self.blocks = []

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n:
            return -1
        traces = {}
        for x in connections:
            traces[x[0]] = traces.get(x[0],[])+[x[1]]
            traces[x[1]] = traces.get(x[1],[])+[x[0]]
        visited = [False for x in range(n)]
        isole = list(filter(lambda x:x not in traces,[x for x in range(n)]))
        for x in isole:
            visited[x] = True 
        res = len(isole)
        parents = [x for x in range(n)]
        for x in isole:
            parents[x] = x
        for i in range(n):
            if not visited[i]:
                self.bfs(parents,traces,i,visited)
        

        return len(set(parents))-1
        
    def bfs(self,parents,traces,cur,visited):
        q = traces[cur]
        parents[cur] = cur
        while q != []:
            tmp = q.pop(0)
            if not visited[tmp]:
                parents[tmp] = cur 
                visited[tmp] = True 
                q += traces[tmp]
            else:
                continue
 
