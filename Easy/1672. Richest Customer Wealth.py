class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_num = 0
        for i in range(len(accounts)):
            if sum(accounts[i])>max_num:
                max_num = sum(accounts[i])
            
        return max_num
            
        
        


sol = Solution()
print(sol.maximumWealth([[1,2,3], [3,2,1]]))