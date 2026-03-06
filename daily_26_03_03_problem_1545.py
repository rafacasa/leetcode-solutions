# Accepted
# Runtime 356 ms Beats 25.29%
# Memory 22.06 MB Beats 41.34%

class Solution:
    def gen_next_str(self, s):
        s1 = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                s1 += "0"
            else:
                s1 += "1"
        return s + "1" + s1

    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        while k > len(s):
            s = self.gen_next_str(s)
        return s[k - 1]


print(Solution().findKthBit(3, 1))
print(Solution().findKthBit(4, 11))
