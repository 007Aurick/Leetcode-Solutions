class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        
        nums1 = []
        for i in range(len(nums)):
            nums1.append(nums[i])

        nums2 = nums1[::-1]

        nums3 = nums1 + nums2


        return nums3

        

sol = Solution()
print(sol.concatWithReverse([1,2,3]))