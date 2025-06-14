from typing import List

# Accepted
# Runtime 15 ms Beats 73.38%
# Memory 19.85 MB Beats 69.51%


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n
        i = 1

        while i < n:
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
            i += 1

        i = n - 2

        while i >= 0:
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
            i -= 1

        return sum(candy)


print(Solution().candy([1, 0, 2]))
print(Solution().candy([1, 2, 2]))
print(Solution().candy([100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60]))
print(Solution().candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]))
print(
    Solution().candy(
        [
            20000,
            20000,
            16001,
            16001,
            16002,
            16002,
            16003,
            16003,
            16004,
            16004,
            16005,
            16005,
            16006,
            16006,
            16007,
            16007,
            16008,
            16008,
            16009,
            16009,
            16010,
            16010,
            16011,
            16011,
            16012,
            16012,
            16013,
            16013,
            16014,
            16014,
            16015,
            16015,
            16016,
            16016,
            16017,
            16017,
            16018,
            16018,
            16019,
            16019,
            16020,
            16020,
            16021,
            16021,
            16022,
            16022,
            16023,
            16023,
            16024,
            16024,
        ]
    )
)
