class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict1 = {}
        list1 = []
        for i in nums:
            dict1[i] = dict1.get(i,0) + 1
        for k,v in dict1.items():
            if v == 2:
                list1.append(k)
        return list1


sol = Solution()
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))
        