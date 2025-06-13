from typing import List

# Memory Limit Exceeded


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [str(i) for i in range(1, n + 1)]
        return sorted(ans)

    def findKthNumber(self, n: int, k: int) -> int:
        return int(self.lexicalOrder(n)[k - 1])


print(Solution().findKthNumber(13, 2))
print(Solution().findKthNumber(1, 1))
