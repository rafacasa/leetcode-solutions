# Accepted
# Runtime 73 ms Beats 53.96%
# Memory 17.56 MB Beats 95.91%


class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        diff = abs(nums[0] - nums[-1])
        for i in range(1, len(nums)):
            diff = max(diff, abs(nums[i - 1] - nums[i]))
        return diff


print(Solution.maxAdjacentDistance([1, 2, 4]))
print(Solution.maxAdjacentDistance([-5, -10, -5]))
