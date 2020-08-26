class Solution:
    
    '''
       [[3],[2,4],[1],[0,4],[1,3]]
        
                 0 R
                 3 B
                 4 R
                 1 B
                 2 R
                 1 B
            
         
    
    '''
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph)==1:
            return len(graph[0])==0
        self.visited = ["*" for x in graph]
        self.res = True
        index = 0
        '''
        max_length = 0
        start = []
        for x in len(graph):
            if(len(x) > max_length):
                max_length = len(x)
                start = x
        '''
        for i in range(len(graph)):
            if not graph[i]:
                continue
            self.visited[i]="R"
            for x in graph[i]:
                self.visited[x] = "B"
            index = i
            break
        for i in range(index+1,len(graph)):
            #print(i," ",self.res," ",self.visited) # 
            if not graph[i]:
                continue
            if self.visited[i]!="*":
                self.bfs(i,graph)
                if not self.res:
                    return False
            #print(i," ",self.res," ",self.visited)
        #print(self.res)
        for i in range(len(graph)):
            if not graph[i]:
                continue
            if self.visited[i]=='*':
                flag = "R"
                for x in graph[i]:
                    if self.visited[i] == 'R':
                        flag = "B"
                    else:
                        flag = "R"
                self.visited[i] = flag
                self.bfs(i,graph)
        return self.res
        
            
        
    def bfs(self,node,graph):
        q = [node]
        while q!=[]:
            l = [x for x in q]
            q = []
            for x in l:
                #print("x = ",x," ","self.visited[x] : ",self.visited[x])
                prochains = graph[x]
                for prochain in prochains:
                    #print("prochain : ",prochain," x = ",x," self.visited[x] : ",self.visited[x])
                    if self.visited[prochain]=="*":
                        if self.visited[x]=="R":
                            self.visited[prochain]="B"
                        else:
                            self.visited[prochain]="R"
                        q.append(prochain)
                    else:
                        if self.visited[prochain]==self.visited[x]:
                            self.res = False
                            return 
                        else:
                            #print(x," : ",prochain," ",self.visited[x])
                            if self.visited[x]=="R":
                                self.visited[prochain]="B"
                            else:
                                self.visited[prochain]="R"
        return  
