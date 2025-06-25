import bisect
from math import ceil

# Accepted
# Runtime 3612 ms Beats 27.00%
# Memory 25.66 MB Beats 86.00%


class Solution:
    def _cnt_products_lt_a_for_single_num1(self, a: int, num1: int) -> int:
        if num1 == 0:
            if a < 0:
                return 0
            return len(self.nums2)

        if num1 > 0:
            search_for = a // num1
            return bisect.bisect(self.nums2, search_for)

        search_for = ceil(a / num1)
        return len(self.nums2) - bisect.bisect_left(self.nums2, search_for)

    def _cnt_products_lt_a(self, a: int) -> int:
        cnt = 0
        for num in self.nums1:
            cnt += self._cnt_products_lt_a_for_single_num1(a, num)
        return cnt

    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        self.nums1 = nums1
        self.nums2 = nums2

        return bisect.bisect_left(
            range(int(-1e10), int(1e10)), k, key=lambda x: self._cnt_products_lt_a(x)
        ) - int(1e10)


print(Solution().kthSmallestProduct(nums1=[2, 5], nums2=[3, 4], k=2))
print(Solution().kthSmallestProduct(nums1=[-4, -2, 0, 3], nums2=[2, 4], k=6))
print(
    Solution().kthSmallestProduct(nums1=[-2, -1, 0, 1, 2], nums2=[-3, -1, 2, 4, 5], k=3)
)
print(Solution().kthSmallestProduct(nums1=[-6], nums2=[-9], k=1))
