# using a DSU calculate MST


class DSU:
    def __init__(self, n):
        self.parents = len(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            self.parents[pa] = pb

        if self.rank[pb] < self.rank[pa]:
            self.parents[pb] = pa

        else:
            self.parents[pb] = pa
            self.rank[pa] += 1
        return True
