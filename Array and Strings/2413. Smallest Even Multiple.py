class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            lcm = n
        elif n%2 != 0:
            lcm = n*2
    
        return lcm


sol = Solution()
print(sol.smallestEvenMultiple(5))