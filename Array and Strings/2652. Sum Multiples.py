class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum_num = 0

        for i in range(1,n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum_num+=i
        
        return sum_num



sol = Solution()
print(sol.sumOfMultiples(7))
        