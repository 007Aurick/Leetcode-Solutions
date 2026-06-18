class Solution:
    def transformArray(self, nums):
        list1 = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                list1.append(0)
            elif nums[i] % 2 == 1:
                list1.append(1)
        list1.sort()

        return list1

sol = Solution()
print(sol.transformArray([4,3,2,1]))
        