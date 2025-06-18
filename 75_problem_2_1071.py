# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.86 MB Beats 45.88%


def gcd(i: int, j: int) -> int:
    a = min(i, j)
    b = max(i, j)
    while a != 0 and b != 0:
        b = b % a
        if a > b:
            b, a = a, b
    return max(a, b)


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        gcd_strings = gcd(l1, l2)
        sstr1 = str1[0:gcd_strings]
        sstr2 = str2[0:gcd_strings]
        if sstr1 == sstr2:
            if (
                sstr1 * (l1 // gcd_strings) == str1
                and sstr1 * (l2 // gcd_strings) == str2
            ):
                return sstr1
        return ""


print(Solution().gcdOfStrings("ABCABC", "ABC"))
print(Solution().gcdOfStrings("ABABAB", "ABAB"))
print(Solution().gcdOfStrings("LEET", "CODE"))
print(gcd(2, 5))
print(gcd(2, 6))
print(gcd(48, 18))
