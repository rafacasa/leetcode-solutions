# Accepted
# Runtime 2971 ms Beats 61.97%
# Memory 18.04 MB Beats 92.96%


class Solution:
    def calculateStatus(self, cnt_a, cnt_b):
        return ((cnt_a % 2) * 2) + (cnt_b % 2)

    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = float("-inf")

        for a in ["0", "1", "2", "3", "4"]:
            for b in ["0", "1", "2", "3", "4"]:
                if a == b:
                    continue

                best = [float("inf")] * 4
                cnt_a = 0
                cnt_b = 0
                prev_a = 0
                prev_b = 0
                left = -1

                for right in range(n):
                    cnt_a += s[right] == a
                    cnt_b += s[right] == b

                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = self.calculateStatus(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        left += 1
                        prev_a += s[left] == a
                        prev_b += s[left] == b

                    right_status = self.calculateStatus(cnt_a, cnt_b)
                    needed_left_status = right_status ^ 0b10

                    if best[needed_left_status] != float("inf"):
                        ans = max(ans, cnt_a - cnt_b - best[needed_left_status])

        return ans


print(Solution().maxDifference("12233", 4))
print(Solution().maxDifference("1122211", 3))
print(Solution().maxDifference("110", 3))
