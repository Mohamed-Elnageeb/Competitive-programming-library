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
    