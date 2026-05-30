class Solution:
    def minimumOperations(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 1:
                nums[i] = nums[i]-1
                count+=1
            elif nums[i] % 3 == 2:
                nums[i] = nums[i]+1
                count+=1
            else:
                count+=0
        return count
sol = Solution()
print(sol.minimumOperations([1,2,3,4]))