# Accepted
# Runtime 67 ms Beats 24.74%
# Memory 20.50 MB Beats 7.08%

class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(d) for d in n])


print(Solution().minPartitions("32"))
print(Solution().minPartitions("82734"))
print(Solution().minPartitions("27346209830709182346"))
