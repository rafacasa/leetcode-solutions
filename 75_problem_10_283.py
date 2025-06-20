# Accepted
# Runtime 9 ms Beats 25.44%
# Memory 19.05 MB Beats 9.61%


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        rigth = 1
        while rigth < n:
            while nums[left] != 0 and left < n:
                left += 1
            if nums[rigth] != 0 and left < rigth:
                nums[left], nums[rigth] = nums[rigth], nums[left]
            rigth += 1
        print(nums)


print(Solution().moveZeroes([0, 1, 0, 3, 12]))
print(Solution().moveZeroes([0]))
