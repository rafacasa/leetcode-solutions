class Solution:
    def partitionString(self, s: str) -> list[str]:
        ans = dict()

        curr = ""
        i = 0
        for letter in s:
            curr += letter
            if curr not in ans:
                ans[curr] = i
                i += 1
                curr = ""
        return [l for l in ans.keys()]


print(Solution().partitionString("abbccccd"))
print(Solution().partitionString("aaaa"))
print(Solution().partitionString("abbccccd"))
