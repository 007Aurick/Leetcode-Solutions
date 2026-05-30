class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = []
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            new_list.append(sums)


            
        return new_list


sol = Solution()
print(sol.runningSum([1,2,3,4]))

        