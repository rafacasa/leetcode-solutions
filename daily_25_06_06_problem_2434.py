# Accepted
# Runtime 2162 ms Beats 5.01%
# Memory 19.28 MB Beats 99.87%

import string
from collections import deque


class Solution:
    def operacao1(self):
        self.t.append(self.s.popleft())

    def operacao2(self):
        self.p += self.t.pop()

    def robotWithString(self, s: str) -> str:
        self.t = deque()
        self.s = deque(s)
        self.p = ""

        for letter in string.ascii_lowercase:
            while self.t and self.t[-1] <= letter:
                self.operacao2()

            while letter in self.s:
                while not self.t or self.t[-1] != letter:
                    self.operacao1()
                self.operacao2()

        return self.p


print(Solution().robotWithString("zza"))
print(Solution().robotWithString("bac"))
print(Solution().robotWithString("bdda"))
print(Solution().robotWithString("mmuqezwmomeplrtskz"))
