# Accepted
# Runtime 43 ms Beats 20.28%
# Memory 37.58 MB Beats 23.65%


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        min1 = nums[0]
        min2 = None

        for i in range(1, n):
            if min2 is not None and nums[i] > min2:
                return True
            if nums[i] > min1:
                min2 = nums[i]
            if nums[i] < min1:
                min1 = nums[i]

        return False


print(Solution().increasingTriplet([1, 2, 3, 4, 5]))
print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))
