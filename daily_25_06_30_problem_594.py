from collections import Counter

# Accepted
# Runtime 27 ms Beats 65.17%
# Memory 19.23 MB Beats 22.00%


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        max_cnt = 0

        for n in cnt.keys():
            if cnt[n + 1]:
                max_cnt = max(max_cnt, cnt[n] + cnt[n + 1])

        return max_cnt


print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
print(Solution().findLHS([1, 2, 3, 4]))
print(Solution().findLHS([1, 1, 1, 1]))
