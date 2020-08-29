class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        stats = {}
        traces = {}
        start,end = min(start,end),max(start,end)
        self.res = 0.0
        for i in range(len(edges)):
            x = edges[i]
            traces[x[0]] = traces.get(x[0],[])+[x[1]]
            traces[x[1]] = traces.get(x[1],[])+[x[0]]
            stats[(x[0],x[1])] = succProb[i]
            stats[(x[1],x[0])] = succProb[i]
        q = [[start,set([start]),1.0]]
        while q!=[]:
            tmp = q.pop(0)
            if tmp[0] not in traces:
                continue
            for x in traces[tmp[0]]:
                prob = tmp[2] * stats[(tmp[0],x)]
                if x in tmp[1]:
                    continue
                if self.res >= prob:
                    continue
                if x==end:
                    self.res = max(self.res,prob)
                else:
                    s = set(tmp[1])
                    s.add(x)
                    q.append([x,s,prob])
        return self.res
