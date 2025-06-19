# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.83 MB Beats 74.66%


class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        prev = chars[0]
        cnt = 1
        j = 0
        if n == 1:
            return 1
        for i in range(1, n):
            if chars[i] == prev:
                cnt += 1
            else:
                chars[j] = prev
                prev = chars[i]
                j += 1
                if cnt > 1:
                    cnt_str = str(cnt)
                    for digit in cnt_str:
                        chars[j] = digit
                        j += 1
                cnt = 1
            if i == n - 1:
                chars[j] = prev
                j += 1
                if cnt > 1:
                    cnt_str = str(cnt)
                    for digit in cnt_str:
                        chars[j] = digit
                        j += 1
        print(chars)
        return j


print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
print(Solution().compress(["a"]))
print(
    Solution().compress(
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    )
)
print(Solution().compress(["a", "b", "c"]))
