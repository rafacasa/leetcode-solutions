import bisect

# Accepted
# Runtime 1016 ms Beats 44.50%
# Memory 71.84 MB Beats 78.57%


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        qtd_events = len(events)
        events.sort()
        starts = [event[0] for event in events]
        dp = [[0] * (qtd_events + 1) for _ in range(k + 1)]

        for curr_idx in range(qtd_events - 1, -1, -1):
            for curr_count in range(1, k + 1):
                next_idx = bisect.bisect(starts, events[curr_idx][1])
                dp[curr_count][curr_idx] = max(
                    dp[curr_count][curr_idx + 1],
                    dp[curr_count - 1][next_idx] + events[curr_idx][2],
                )

        return dp[k][0]


print(Solution().maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2))
print(Solution().maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2))
print(Solution().maxValue([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3))
print(Solution().maxValue([[1, 3, 4], [2, 4, 1], [1, 1, 4], [3, 5, 1], [2, 5, 5]], 3))
