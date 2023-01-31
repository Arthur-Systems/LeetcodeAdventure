
class Solution:
    def PowerOfN(self, X, N):
        if N == 0:
            return 1
        if N == 1:
            return X
        if N % 2 == 0:
            return self.PowerOfN(X, N//2) * self.PowerOfN(X, N//2)
        else:
            return self.PowerOfN(X, N // 2) * self.PowerOfN(X, N // 2) * X


if __name__ == "__main__":
    N = 12
    X = 3
    print(Solution().PowerOfN(X, N))
