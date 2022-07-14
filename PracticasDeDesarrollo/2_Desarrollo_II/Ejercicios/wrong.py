from typing import Dict


def mul(num, alt: bool = False):
    if alt:
        return num * 5
    return num * -2


b: Dict = mul(23, "wrong")


class Mistery:
    def __init__(x, y, z):
        self.x = x
        self.y = y

    def funtionX(self) -> int:
        ans = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for a, b in zip(self.x, self.x[1:]):
            if roman[a] < roman[b]:
                ans -= roman[a]
            else:
                ans += roman[a]

        return ans + roman[self.x[-1]]

    def functionY(self, target) -> List[int]:
        numToIndex = {}

        for i, num in enumerate(self.y):
            if target - num in numToIndex:
                return numToIndex[target - num], i
        numToIndex[num] = i
