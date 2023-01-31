class Solution:
    def Fibonacci(self, n):
        if n == 1 or n == 2:
            return n
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    def FibonacciDynamic(self, n):
        if n == 1 or n == 2:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]


if __name__ == "__main__":
    number = 10
    print(Solution().Fibonacci(number))
