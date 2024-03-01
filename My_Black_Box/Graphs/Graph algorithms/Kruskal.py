from array import array 

class disjointset:
    def __init__(self, n):
        self.rank, self.parent = array('i', [0] * (n + 1)), array('i', [i for i in range(n + 1)])
        self.n, self.even = n, array('b', [0] * (n + 1))
        self.sz = [1]* (n+1)
 
    def find(self, x):
        xcopy = x
        while x != self.parent[x]: x = self.parent[x]
        while xcopy != x:
            self.parent[xcopy], xcopy = x, self.parent[xcopy]
        return x
    
    def union(self, x, y):
        xpar, ypar = self.find(x), self.find(y)
 
        if xpar == ypar: return 1
 
        par, child = xpar, ypar
        if self.rank[xpar] < self.rank[ypar]:
            par, child = ypar, xpar
 
        elif self.rank[xpar] == self.rank[ypar]:
            self.rank[xpar] += 1
 
        self.parent[child] = par
        k = self.sz[par] + self.sz[child] 
        self.sz[par] = k 
        self.sz[child] = k
        self.even[par] |= self.even[child]
        self.n -= 1
        return 0 
    

def kruskal(n,edges) : 
    ds = disjointset(n) 
    edges.sort(reverse = 0) 
    # path = []  
    ans = 0 
    e = 0 
    for w,u,v in edges : 
        if ds.find(u) != ds.find(v) : 
            ds.union(u,v) 
            ans += w
            e += 1
            # path.append((u,v)) 
        if e == n-1 : 
            return ans 
            
    return -1 
        
    
