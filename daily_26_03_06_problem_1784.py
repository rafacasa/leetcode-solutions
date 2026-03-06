# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 19.39 MB Beats 41.18%

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seg1 = True
        for l in s:
            if l == "0":
                seg1 = False
            else:
                if not seg1:
                    return False
        return True


print(Solution().checkOnesSegment("1001"))
print(Solution().checkOnesSegment("110"))
