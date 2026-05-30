class Solution:
    def alternatingSum(self, nums):
        list1 = []
        for i in range(len(nums)):
            if i%2==1:
                list1.append(nums[i]*-1)

            else:
                list1.append(nums[i])
        return sum(list1)


sol = Solution()
print(sol.alternatingSum([1,3,5,7]))
        