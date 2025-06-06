# Accepted
# Runtime 11 ms Beats 15.54%
# Memory 17.93 MB Beats 20.63%


class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        prev = None
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        map_prev = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"],
        }

        for letter in s:
            if prev:
                if letter in map_prev[prev]:
                    value += values[letter]
                    value -= values[prev]
                    prev = None
                    continue
                else:
                    value += values[prev]
                    prev = None

            if letter in map_prev:
                prev = letter
                continue

            value += values[letter]

        if prev:
            value += values[prev]

        return value
