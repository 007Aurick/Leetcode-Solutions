class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_map = {}
        t_map = {}

        
        for i in range(len(s)):
            s_map[s[i]] = i
            t_map[t[i]] = i

        sum_nums = 0
        for char in s:
            sum_nums += abs(s_map[char]-t_map[char])
        return sum_nums

            
       
sol = Solution()
print(sol.findPermutationDifference("abc", "bac"))