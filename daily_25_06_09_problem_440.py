# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.83 MB Beats 35.88%


class Solution:
    def get_cnt_edges(self, start: int, n: int) -> int:
        cnt = 0
        left = start * 10
        right = left + 9

        while right <= n:
            cnt += right - left + 1
            left *= 10
            right = right * 10 + 9

        if left <= n:
            cnt += n - left + 1

        return cnt

    def findKthNumber(self, n: int, k: int) -> int:
        n_step = 1
        k_step = 1

        while k_step != k:
            cnt = self.get_cnt_edges(n_step, n)
            if k_step + cnt < k:
                n_step += 1
                k_step += cnt + 1
            else:
                n_step *= 10
                k_step += 1

        return n_step


print(Solution().findKthNumber(13, 2))
print(Solution().findKthNumber(1, 1))
