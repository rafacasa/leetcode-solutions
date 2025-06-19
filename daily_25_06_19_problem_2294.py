from typing import List

# Accepted
# Runtime 75 ms Beats 92.99%
# Memory 29.06 MB Beats 73.61%


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_group = nums[0]
        max_group_limit = min_group + k
        cnt = 1
        n = len(nums)

        for i in range(n):
            if nums[i] > max_group_limit:
                cnt += 1
                max_group_limit = nums[i] + k

        return cnt


print(Solution().partitionArray([3, 6, 1, 2, 5], k=2))
print(Solution().partitionArray([1, 2, 3], k=1))
print(Solution().partitionArray([2, 2, 4, 5], k=0))
