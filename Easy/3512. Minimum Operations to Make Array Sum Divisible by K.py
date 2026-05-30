import random
class Solution:
    def minOperations(self, nums, k):
        count = 0
        i = random.randint(0,len(nums)-1)
        while sum(nums) % k != 0:
            nums[i] = nums[i]-1
            count+=1
            
        return count
sol = Solution()
print(sol.minOperations([3,9,7],5))