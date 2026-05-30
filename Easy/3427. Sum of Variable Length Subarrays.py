class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        sum_nums = 0

        for i in range(len(nums)):
            start = max(0,i-nums[i])
            if start == i:
                sum_nums += nums[i]
            else:
                for x in range(start, i+1):
                    sum_nums+=nums[x]

        return sum_nums

        
sol = Solution()
print(sol.subarraySum([2,3,1]))
        