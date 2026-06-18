class Solution:
    def getConcatenation(self, nums):
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
sol = Solution()
print(sol.getConcatenation([1,2,1]))