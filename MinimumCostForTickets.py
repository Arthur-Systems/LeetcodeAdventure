class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        day_set = set(days)  # To quickly check if a day is a travel day
        max_day = days[-1]   # Last travel day
        dp = [0] * (max_day + 1)

        for day in range(1, max_day + 1):
            if day not in day_set:
                # If not a travel day, cost is the same as the previous day
                dp[day] = dp[day - 1]
            else:
                # Minimum cost by taking 1-day, 7-day, or 30-day pass
                dp[day] = min(
                    dp[max(0, day - 1)] + costs[0],  # 1-day pass
                    dp[max(0, day - 7)] + costs[1],  # 7-day pass
                    dp[max(0, day - 30)] + costs[2]  # 30-day pass
                )

        return dp[max_day]


if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    sol = Solution()
    print(sol.mincostTickets(days, costs))  # Output: 11
