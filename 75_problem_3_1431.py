from typing import List

# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.97 MB Beats 12.31%


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = []
        for i in candies:
            ans.append(i + extraCandies >= max_candies)
        return ans


print(Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))
print(Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))
print(Solution().kidsWithCandies([12, 1, 12], 10))
