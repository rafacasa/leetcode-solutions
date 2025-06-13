# Accepted
# Runtime 483 ms Beats 75.45%
# Memory 23.21 MB Beats 87.57%

import string
from collections import deque


class Solution:
    def clearStars(self, s: str) -> str:
        cnt_letters = {a: deque() for a in string.ascii_lowercase}
        ans = list(s)
        for i, letter in enumerate(s):
            if letter == "*":
                for find_letter in string.ascii_lowercase:
                    if cnt_letters[find_letter]:
                        ans[cnt_letters[find_letter].pop()] = "*"
                        break
            else:
                cnt_letters[letter].append(i)

        return "".join(c for c in ans if c != "*")


print(Solution().clearStars("aaba*"))
print(Solution().clearStars("abc"))
