# Accepted
# Runtime 43 ms Beats 12.53%
# Memory 26.03 MB Beats 29.30%


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix_product = [0] * n
        suffix_product = [0] * n

        i, j = 1, n - 2

        prefix_product[0] = nums[0]
        suffix_product[-1] = nums[-1]
        while i < n and j > -1:
            prefix_product[i] = prefix_product[i - 1] * nums[i]
            suffix_product[j] = suffix_product[j + 1] * nums[j]
            i += 1
            j -= 1

        ans = list()
        for i in range(n):
            pre = 1 if i == 0 else prefix_product[i - 1]
            suf = 1 if i == n - 1 else suffix_product[i + 1]
            ans.append(pre * suf)

        return ans


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
