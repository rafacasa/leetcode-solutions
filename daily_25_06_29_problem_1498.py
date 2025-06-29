import bisect

# Accepted
# Runtime 340 ms Beats 52.43%
# Memory 27.95 MB Beats 56.17%


MOD = 10**9 + 7


# https://cp-algorithms.com/algebra/binary-exp.html
def fast_pow(base: int, exponent: int) -> int:
    base = base % MOD
    ans = 1
    while exponent:
        if exponent & 1:
            ans = ans * base % MOD
        base = base * base % MOD
        exponent >>= 1
    return ans


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i, num1 in enumerate(nums):
            if 2 * num1 > target:
                continue
            max_j = bisect.bisect(nums, target - num1) - 1
            ans += fast_pow(2, max_j - i)
            ans %= MOD
        return ans


print(Solution().numSubseq([3, 5, 6, 7], target=9))
print(Solution().numSubseq([3, 3, 6, 8], target=10))
print(Solution().numSubseq([2, 3, 3, 4, 6, 7], target=12))
print(
    Solution().numSubseq(
        [
            14,
            4,
            6,
            6,
            20,
            8,
            5,
            6,
            8,
            12,
            6,
            10,
            14,
            9,
            17,
            16,
            9,
            7,
            14,
            11,
            14,
            15,
            13,
            11,
            10,
            18,
            13,
            17,
            17,
            14,
            17,
            7,
            9,
            5,
            10,
            13,
            8,
            5,
            18,
            20,
            7,
            5,
            5,
            15,
            19,
            14,
        ],
        target=22,
    )
)
