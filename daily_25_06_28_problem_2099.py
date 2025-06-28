# Accepted
# Runtime 15 ms Beats 11.38%
# Memory 18.00 MB Beats 78.57%


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        ans = []
        sorted_nums = sorted(nums, reverse=True)
        sorted_nums = sorted_nums[:k]

        for num in nums:
            if num in sorted_nums:
                ans.append(num)
                sorted_nums.remove(num)
            if not sorted_nums:
                break

        return ans


# Accepted
# Runtime 3 ms Beats 83.73%
# Memory 17.88 MB Beats 94.31%


class Solution_2:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        aux = [(i, nums[i]) for i in range(len(nums))]
        aux.sort(key=lambda x: x[1], reverse=True)
        aux = sorted(aux[:k], key=lambda x: x[0])
        return [num for i, num in aux]


print(Solution().maxSubsequence([2, 1, 3, 3], k=2))
print(Solution().maxSubsequence([-1, -2, 3, 4], k=3))
print(Solution().maxSubsequence([3, 4, 3, 3], k=2))
print(Solution_2().maxSubsequence([2, 1, 3, 3], k=2))
print(Solution_2().maxSubsequence([-1, -2, 3, 4], k=3))
print(Solution_2().maxSubsequence([3, 4, 3, 3], k=2))
