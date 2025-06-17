# Solution MLE


MOD = 10**9 + 7


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


class Solution:
    def __init__(self):
        self.fat = {0: 1, 1: 1}

    def fatorial(self, n: int):
        temp = self.fat.get(n, None)
        if temp:
            return temp
        temp = n * self.fatorial(n - 1)
        self.fat[n] = temp
        return temp

    def comb(self, n: int, k: int):
        return self.fatorial(n) / (self.fatorial(k) * self.fatorial(n - k))

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return int(self.comb(n - 1, k) * ((m - 1) ** (n - k - 1)) * m)


a = Solution()

print(a.countGoodArrays(3, 2, 1))
print(a.countGoodArrays(4, 2, 2))
print(a.countGoodArrays(5, 2, 0))
print(a.countGoodArrays(40603, 16984, 29979))
