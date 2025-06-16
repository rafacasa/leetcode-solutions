from typing import List

# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.83 MB Beats 59.91%


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = float("inf")
        max_diff = float("-inf")

        for num in nums:
            min_num = min(min_num, num)
            diff = num - min_num
            if diff > 0:
                max_diff = max(max_diff, diff)

        if max_diff == float("-inf"):
            max_diff = -1
        return max_diff


print(Solution().maximumDifference([7, 1, 5, 4]))
print(Solution().maximumDifference([9, 4, 3, 2]))
print(Solution().maximumDifference([1, 5, 2, 10]))
