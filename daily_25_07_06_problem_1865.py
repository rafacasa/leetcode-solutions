from collections import Counter

# Accepted
# Runtime 299 ms Beats 43.79%
# Memory 48.36 MB Beats 68.98%


class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt_n2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.cnt_n2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.cnt_n2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0

        for num in self.nums1:
            needs = tot - num
            if needs in self.cnt_n2:
                ans += self.cnt_n2[needs]

        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
