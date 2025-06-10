# Accepted
# Runtime 5446 ms Beats 6.79%
# Memory 17.74 MB Beats 50.54%


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        qtd = 0
        for i in range(min(n, limit) + 1):
            qtd += max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)
        return qtd


print(Solution().distributeCandies(5, 2))
print(Solution().distributeCandies(3, 3))
print(Solution().distributeCandies(10001, 20002))
