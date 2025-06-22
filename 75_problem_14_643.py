# Accepted
# Runtime 95 ms Beats 35.86%
# Memory 27.46 MB Beats 39.23%


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = last_sum = sum(nums[:k])

        for i in range(1, len(nums) - k + 1):
            # max_sum = max(max_sum, sum(nums[i : i + k]))
            last_sum = last_sum + (nums[i + k - 1] - nums[i - 1])
            max_sum = max(max_sum, last_sum)
        return max_sum / k


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(Solution().findMaxAverage([5], 1))
