# Memory Limit Exceeded


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        nums = [str(i + 1) for i in range(n)]
        nums.sort()
        return int(nums[k - 1])


print(Solution().findKthNumber(13, 2))
print(Solution().findKthNumber(1, 1))
