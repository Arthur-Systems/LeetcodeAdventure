import timeit


def RecursiveFibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return RecursiveFibonacci(n - 1) + RecursiveFibonacci(n - 2)


def IterativeFibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


def DyanmicFibonacci(n):
    dp = [None] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def DyanmicRecursiveFibonacci(n, dp):
    if n == 0:
        dp[n] = 0
        return dp[n]
    if n == 1:
        dp[n] = 1
        return dp[n]
    if dp[n] != None:
        return dp[n]
    dp[n] = DyanmicRecursiveFibonacci(
        n - 1, dp) + DyanmicRecursiveFibonacci(n - 2, dp)
    return dp[n]


if __name__ == "__main__":
    Number = 100
    print(IterativeFibonacci(Number))
    print(DyanmicFibonacci(Number))
    print(DyanmicRecursiveFibonacci(Number, [None] * (Number + 1)))
    print(RecursiveFibonacci(Number))
