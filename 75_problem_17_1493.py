# Accepted
# Runtime 95 ms Beats 8.22%
# Memory 21.80 MB Beats 67.50%


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = rigth = 0
        cnt_zeros = 0
        max_digits = 0

        while rigth < len(nums):
            if nums[rigth] == 0:
                cnt_zeros += 1
            while cnt_zeros > 1 and left <= rigth:
                if nums[left] == 0:
                    cnt_zeros -= 1
                left += 1
            max_digits = max(max_digits, rigth - left + 1 - cnt_zeros)
            rigth += 1

        if max_digits == len(nums):
            return max(max_digits - 1, 0)
        return max_digits


print(Solution().longestSubarray([1, 1, 0, 1]))
print(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(Solution().longestSubarray([1, 1, 1]))
