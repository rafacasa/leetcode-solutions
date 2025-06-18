from typing import List

# Accepted
# Runtime 75 ms Beats 86.92%
# Memory 33.20 MB Beats 69.20%


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        i = 2
        ans = []
        while i < len(nums):
            if nums[i] - nums[i - 2] > k:
                return []
            ans.append([nums[i - 2], nums[i - 1], nums[i]])
            i += 3
        return ans


print(Solution().divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
print(Solution().divideArray([2, 4, 2, 2, 5, 2], 2))
print(
    Solution().divideArray(
        [4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14
    )
)
