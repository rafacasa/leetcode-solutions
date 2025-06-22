class Solution:
    def is_prime(self, num: int) -> bool:
        primes = [3, 5, 7, 11]
        if num in primes:
            return True
        elif num < 2:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False
        else:
            for prime in primes:
                if num % prime == 0:
                    return False
            return True

    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        cnt = {}

        for num in nums:
            cnt_num = cnt.get(num, 0)
            cnt[num] = cnt_num + 1

        for cnt_num in cnt.values():
            if self.is_prime(cnt_num):
                return True
        return False


print(Solution().checkPrimeFrequency([1, 2, 3, 4, 5, 4]))
print(Solution().checkPrimeFrequency([1, 2, 3, 4, 5]))
print(Solution().checkPrimeFrequency([2, 2, 2, 4, 4]))
print(Solution().checkPrimeFrequency([1, 1, 11, 4, 8, 1]))
