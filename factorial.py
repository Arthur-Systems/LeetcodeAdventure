
class Solution:
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)

    def factorialDynamic(self, n):
        if n == 0:
            return 1
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[i-1] * (i+1)
        return dp[n-1]


if __name__ == "__main__":
    number = 1000
    print(Solution().factorialDynamic(number))
