class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False

        # union by rank
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        if self.rank[pb] < self.rank[pa]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1
        return True
