class Solution:
    def reverseDegree(self, s: str) -> int:

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        reverse_alpha = alphabet[::-1]

        sum_nums = 0
        for i in range(len(s)):
            for j in range(len(reverse_alpha)):
                if s[i] == reverse_alpha[j]:
                    product = (i+1)*(j+1)
                    sum_nums += product

        return sum_nums

sol = Solution()
print(sol.reverseDegree("abc"))