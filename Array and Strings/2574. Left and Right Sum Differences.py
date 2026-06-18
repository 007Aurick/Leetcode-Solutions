class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []
        x = nums[::-1]
        sum_left = 0
        for i in range(len(nums)):
            if i == 0:
                leftSum.append(0)
            else:
                sum_left+= nums[i-1]
                leftSum.append(sum_left)

        sum_right = 0
        for i in range(len(x)):
            if i == 0:
                rightSum.append(0)
            else:
                sum_right += x[i-1]
                rightSum.append(sum_right)
        
        y = rightSum[::-1]

        result = [abs(a-b) for a,b in zip(y,leftSum)]

        return result

        

sol = Solution()
print(sol.leftRightDifference([10,4,8,3]))
        