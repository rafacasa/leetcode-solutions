# Accepted
# Runtime 9 ms Beats 36.38%
# Memory 18.78 MB Beats 39.11%


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        rigth_sum = sum(nums)

        for i, num in enumerate(nums):
            rigth_sum -= num
            if left_sum == rigth_sum:
                return i
            left_sum += num

        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([1, 2, 3]))
print(Solution().pivotIndex([2, 1, -1]))
