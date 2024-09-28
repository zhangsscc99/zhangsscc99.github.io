class UF:
    def __init__(self, n):
        self._count = n 
        self.parent = [i for i in range(n)]
        self.size = [1 for _ In range(n)]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return 
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ 
            self.size[rootQ] += self.size[rootQ]
        # self.parent[rootP] = rootQ 
        self._count -= 1
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    
    def count(self):
        return self._count
    def connected(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q