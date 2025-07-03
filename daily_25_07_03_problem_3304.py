import string

# Accepted
# Runtime 7 ms Beats 79.00%
# Memory 17.70 MB Beats 85.53%


MAP_CHARS = dict()


def generate_chars():
    if len(MAP_CHARS) == 0:
        for i, c in enumerate(string.ascii_lowercase):
            if c == "z":
                MAP_CHARS[c] = string.ascii_lowercase[0]
                continue
            MAP_CHARS[c] = string.ascii_lowercase[i + 1]


class Solution:
    def kthCharacter(self, k: int) -> str:
        generate_chars()
        ans = "a"

        while len(ans) < k:
            temp = [
                ans,
            ]
            for letter in ans:
                temp.append(MAP_CHARS[letter])
            ans = "".join(temp)
        return ans[k - 1]


print(Solution().kthCharacter(5))
print(Solution().kthCharacter(10))
print(Solution().kthCharacter(500))
