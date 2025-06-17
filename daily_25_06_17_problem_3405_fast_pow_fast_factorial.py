# Accepted
# Runtime 15 ms Beats 91.67%
# Memory 25.15 MB Beats 27.78%

MOD = 10**9 + 7
MAX = 10**5

fat = [0] * MAX
inv_fat = [0] * MAX


# https://cp-algorithms.com/algebra/binary-exp.html
def fast_pow(base: int, exponent: int) -> int:
    base = base % MOD
    ans = 1
    while exponent:
        if exponent & 1:
            ans = ans * base % MOD
        base = base * base % MOD
        exponent >>= 1
    return ans


def pre_calc_fat():
    if fat[0] != 0:
        return

    fat[0] = 1
    for i in range(1, MAX):
        fat[i] = fat[i - 1] * i % MOD

    inv_fat[MAX - 1] = fast_pow(fat[MAX - 1], MOD - 2)
    for i in range(MAX - 1, 0, -1):
        inv_fat[i - 1] = inv_fat[i] * i % MOD


def comb(n: int, k: int):
    return fat[n] * (inv_fat[k] * inv_fat[n - k] % MOD) % MOD


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        pre_calc_fat()
        return (m * (fast_pow(m - 1, n - k - 1)) % MOD) * comb(n - 1, k) % MOD
        int(self.comb(n - 1, k) * ((m - 1) ** (n - k - 1)) * m)


a = Solution()

print(a.countGoodArrays(3, 2, 1))
print(a.countGoodArrays(4, 2, 2))
print(a.countGoodArrays(5, 2, 0))
print(a.countGoodArrays(40603, 16984, 29979))
