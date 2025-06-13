# Accepted
# Runtime 471 ms Beats 23.08%
# Memory 32.66 MB Beats 40.08%

from typing import List


class Solution:
    def count_pairs(self, threshold):
        cnt, i = 0, 0

        while i < len(self.nums) - 1:
            if self.nums[i + 1] - self.nums[i] <= threshold:
                cnt += 1
                i += 1
            i += 1
        return cnt

    def minimizeMax(self, nums: List[int], p: int) -> int:
        self.nums = sorted(nums)

        left = 0
        right = self.nums[-1] - self.nums[0]

        while left < right:
            mid = left + (right - left) // 2
            valid_pairs = self.count_pairs(mid)
            if valid_pairs >= p:
                right = mid
            else:
                left = mid + 1
        return left


print(Solution().minimizeMax([10, 1, 2, 7, 1, 3], 2))
print(Solution().minimizeMax([4, 2, 1, 2], 1))
