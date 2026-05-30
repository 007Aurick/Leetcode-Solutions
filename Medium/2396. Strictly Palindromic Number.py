import numpy as np

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            str_num = np.base_repr(n, i)
            if str_num != str_num[::-1]:
                return False
        return True

sol = Solution()
print(sol.isStrictlyPalindromic(9))