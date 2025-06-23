import string
from collections import deque


def to_base(n: int, k: int) -> str:
    ans = ""
    while n:
        ans += str(n % k)
        n //= k
    return ans[::-1] or "0"


def check_k_mirror(num: int, k: int) -> bool:
    num_k = to_base(num, k)

    left = 0
    right = len(num_k) - 1

    while left < right:
        if num_k[left] != num_k[right]:
            return False
        left += 1
        right -= 1
    return True


palindromes = {}


def generate_palindromes(n_digits: int) -> list:
    dec_palin = palindromes.get(n_digits, False)
    if dec_palin:
        return dec_palin

    if n_digits == 0:
        return []

    mount_digits = deque("123456789")
    if n_digits == 1:
        return [int(num) for num in mount_digits]

    cnt_digits = n_digits // 2
    add_center = n_digits % 2 == 1
    next_level = deque()

    for i in range(1, cnt_digits):
        for num in mount_digits:
            for d in string.digits:
                next_level.append(num + d)
        mount_digits = next_level
        next_level = deque()

    ans = list()

    for left in mount_digits:
        rigth = left[::-1]
        if add_center:
            for d in string.digits:
                ans.append(int(left + d + rigth))
        else:
            ans.append(int(left + rigth))

    palindromes[n_digits] = ans
    return ans


# Accepted
# Runtime 3544 ms Beats 48.26%
# Memory 67.26 MB Beats 8.14%


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        sum_k_mirrors = 0
        cnt_k_mirrors = 0
        digits = 1

        while cnt_k_mirrors < n:
            dec_palin = generate_palindromes(digits)

            for palin_num in dec_palin:
                if check_k_mirror(palin_num, k):
                    sum_k_mirrors += palin_num
                    cnt_k_mirrors += 1
                    if cnt_k_mirrors == n:
                        return sum_k_mirrors
            digits += 1


print(Solution().kMirror(2, 5))
print(Solution().kMirror(3, 7))
print(Solution().kMirror(7, 17))
