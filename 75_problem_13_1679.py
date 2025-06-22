# Accepted
# Runtime 510 ms Beats 46.93%
# Memory 29.89 MB Beats 79.65%


# 2 pointers
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ops = 0

        while left < right:
            v_sum = nums[right] + nums[left]
            if v_sum > k:
                right -= 1
            elif v_sum < k:
                left += 1
            else:
                ops += 1
                left += 1
                right -= 1

        return ops


# Accepted
# Runtime 514 ms Beats 37.68%
# Memory 30.70 MB Beats 27.83%


# Hashmap
class Solution_Hashmap:
    def maxOperations(self, nums: list[int], k: int) -> int:
        cnt_digits = {}
        for num in nums:
            cnt = cnt_digits.get(num, 0)
            cnt_digits[num] = cnt + 1

        ops = 0
        for num in nums:
            if cnt_digits[num] == 0:
                continue
            if cnt_digits.get(k - num, 0) > 0:
                if num == k - num:
                    ops += cnt_digits[num] // 2
                else:
                    ops += min(cnt_digits[num], cnt_digits[k - num])
                    cnt_digits[k - num] = 0
                cnt_digits[num] = 0
        return ops


print(Solution_Hashmap().maxOperations([1, 2, 3, 4], 5))
print(Solution_Hashmap().maxOperations([3, 1, 3, 4, 3], 6))
