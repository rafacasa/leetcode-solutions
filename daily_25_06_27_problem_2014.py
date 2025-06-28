from collections import Counter, deque

# Accepted
# Runtime 894 ms Beats 63.38%
# Memory 17.96 MB Beats 60.56%


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        valid_chars = sorted(
            [char for char, cnt in Counter(s).items() if cnt >= k], reverse=True
        )
        queue = deque(valid_chars)

        while queue:
            current = queue.popleft()
            if len(current) > len(ans):
                ans = current

            for char in valid_chars:
                new_sseq = current + char
                iterator = iter(s)

                if all(ch in iterator for ch in new_sseq * k):
                    queue.append(new_sseq)
        return ans


print(Solution().longestSubsequenceRepeatedK(s="letsleetcode", k=2))
print(Solution().longestSubsequenceRepeatedK(s="bb", k=2))
print(Solution().longestSubsequenceRepeatedK(s="ab", k=2))
