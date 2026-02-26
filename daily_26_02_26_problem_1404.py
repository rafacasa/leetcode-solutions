# Accepted
# Runtime 61 ms Beats 5.11%
# Memory 19.32 MB Beats 54.01%

class Solution:
    def sum_str(self, s: str) -> str:
        len_s = len(s)
        run = True
        ans = []
        for i in range(len_s - 1, -1, -1):
            if run:
                if s[i] == "1":
                    ans.insert(0, "0")
                else:
                    ans.insert(0, "1")
                    run = False
            else:
                ans.insert(0, s[i])
        if run:
            ans.insert(0, "1")
        return "".join(ans)

    def numSteps(self, s: str) -> int:
        steps = 0
        while not s == "1":
            if s[-1] == "0":
                s = s[:-1]
            else:
                s = self.sum_str(s)
            steps += 1
        return steps

if __name__ == "__main__":
    print(Solution().numSteps("1101"))
    print(Solution().numSteps("10"))
    print(Solution().numSteps("1"))
