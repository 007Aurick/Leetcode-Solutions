class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        sums = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                sums+=1
            else:
                sums += 0
        return sums



sol = Solution()
print(sol.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
        