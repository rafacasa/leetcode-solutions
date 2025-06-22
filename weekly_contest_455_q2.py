class Solution:
    def findCoins(self, numWays: list[int]) -> list[int]:
        n = len(numWays)
        coins = []
        dp = [1] + [0] * n
        for i in range(len(numWays)):
            if len(coins) == 0:
                if numWays[i] == 1:
                    coins.append(i + 1)
                    for x in range(i + 1, n + 1):
                        dp[x] += dp[x - i - 1]
                    continue
                if numWays[i] > 1:
                    return []
                continue

            if numWays[i] == dp[i + 1]:
                continue
            if numWays[i] == dp[i + 1] + 1:
                coins.append(i + 1)
                for x in range(i + 1, n + 1):
                    dp[x] += dp[x - i - 1]
                continue
            return []
        return coins


print(Solution().findCoins([0, 1, 0, 2, 0, 3, 0, 4, 0, 5]))
print(Solution().findCoins([1, 2, 2, 3, 4]))
print(Solution().findCoins([1, 2, 3, 4, 15]))
