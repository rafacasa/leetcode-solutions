# Accepted
# Runtime 185 ms Beats 27.55%
# Memory 17.84 MB Beats 90.91%


class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        ans = set()
        for j, num in enumerate(nums):
            if num == key:
                min_idx = max(0, j - k)
                max_idx = min(n - 1, j + k)
                for i in range(min_idx, max_idx + 1):
                    ans.add(i)
        return list(ans)


print(Solution().findKDistantIndices([3, 4, 9, 1, 3, 9, 5], key=9, k=1))
print(Solution().findKDistantIndices([2, 2, 2, 2, 2], key=2, k=2))
