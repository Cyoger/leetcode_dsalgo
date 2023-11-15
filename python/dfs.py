from collections import defaultdict

class graph:
    
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def DFSUtil(self, u, v):
        v.add(u)
        
        print(u, end=' ')
        
        for neighbor in self.graph[u]:
            if neighbor not in v:
                self.DFSUtil(neighbor, v)
                
    def DFS(self, u):
        v = set()
        self.DFSUtil(u, v)
        
        
        
g = graph()

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
print(g.graph)