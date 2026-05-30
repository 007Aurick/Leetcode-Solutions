class Solution:
    def maxDistinct(self, s: str) -> int:
        count = 0
        my_table = {}
        for i in range(len(s)):
           if s[i] not in my_table.values():
              my_table[i] = s[i]
              count+=1
           
        
        return count

sol = Solution()
print(sol.maxDistinct("abab"))