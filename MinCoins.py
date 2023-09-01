def FindMin(coin: list[int], Value: int) -> int:
    dp = [0] * (Value + 1)
    dp[0] = 0
    for i in range(1, Value + 1):
        dp[i] = i
        for j in range(len(coin)):
            if i >= coin[j]:
                dp[i] = min(dp[i], dp[i - coin[j]] + 1)
    return dp[Value]


def FindMinRecursive(coin: list[int], Value: int) -> int:
    if Value <= 0:
        return 0
    mincoins = float('inf')
    for c in coin:
        if Value >= c:
            mincoins = min(mincoins, FindMinRecursive(
                coin, Value - c) + 1)
    return mincoins


def DyanmicRecursive(coin: list[int], Value: int, dp: list[any]) -> int:
    if dp[Value] is not None:
        return dp[Value]
    if Value == 0:
        dp[Value] = 0
        return dp[Value]
    mincoins = float('inf')
    for c in coin:
        if Value >= c:
            mincoins = min(mincoins, DyanmicRecursive(
                coin, Value - c, dp) + 1)
    dp[Value] = mincoins
    return dp[Value]


if __name__ == "__main__":
    coins = [1, 2, 3, 5, 50, 100]
    Value = 100
    print(FindMin(coins, Value))
    print(DyanmicRecursive(coins, Value, [None] * (Value + 1)))
    print(FindMinRecursive(coins, Value))

    assert FindMin(coins, Value) == FindMinRecursive(coins, Value)
