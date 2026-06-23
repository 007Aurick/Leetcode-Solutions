class Solution:
    def isPalindrome(self, x: int) -> bool:

        num = str(x)

        if num == num[::-1]:
            return True
        else:
            return False



sol = Solution()
print(sol.isPalindrome(121))
        