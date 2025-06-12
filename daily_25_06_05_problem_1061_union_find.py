# Accepted
# Runtime 3 ms Beats 92.25%
# Memory 17.83 MB Beats 64.84%


class UnionFind:
    def __init__(self):
        self.parents = dict()

    def find(self, a):
        immediate = self.parents.get(a, a)
        if a == immediate:
            return a
        par_a = self.find(immediate)
        self.parents[a] = par_a
        return par_a

    def union(self, a, b):
        par_a = self.find(a)
        par_b = self.find(b)
        if par_a < par_b:
            self.parents[par_b] = par_a
        else:
            self.parents[par_a] = par_b


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union = UnionFind()
        for i in range(len(s1)):
            union.union(s1[i], s2[i])

        ans = ""
        for letter in baseStr:
            ans += union.find(letter)

        return ans


print(Solution().smallestEquivalentString("parker", "morris", "parser"))
print(Solution().smallestEquivalentString("hello", "world", "hold"))
print(Solution().smallestEquivalentString("leetcode", "programs", "sourcecode"))
