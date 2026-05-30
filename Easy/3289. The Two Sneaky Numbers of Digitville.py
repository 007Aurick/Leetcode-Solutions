class Solution:
    def getSneakyNumbers(self, nums):
        list1 = []
        for i in range(len(nums)):
            if nums[i] in nums[i+1:len(nums)]:
                list1.append(nums[i])
           
        return list1

sol = Solution()
print(sol.getSneakyNumbers([0,1,1,0]))
        