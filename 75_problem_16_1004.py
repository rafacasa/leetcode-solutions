# Accepted
# Runtime 79 ms Beats 17.98%
# Memory 18.35 MB Beats 40.36%


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = rigth = 0
        cnt_zeros = 0
        max_digits = 0

        while rigth < len(nums):
            if nums[rigth] == 0:
                cnt_zeros += 1
            while cnt_zeros > k and left <= rigth:
                if nums[left] == 0:
                    cnt_zeros -= 1
                left += 1
            max_digits = max(max_digits, rigth - left + 1)
            rigth += 1

        return max_digits


print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(
    Solution().longestOnes(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3
    )
)
print(Solution().longestOnes([0, 0, 0, 1], 4))
print(Solution().longestOnes([0, 0, 1, 1, 1, 0, 0], 0))
