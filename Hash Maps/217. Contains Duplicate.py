class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d1 = {}
        list1 = []
        for i in nums:
            d1[i] = d1.get(i,0) +1
        
        for val in d1.values():
            if val>1:
                list1.append(True)
            else:
                list1.append(False)
                
        if True in list1:
            return True
        else:
            return False
        
       

        
sol = Solution()
print(sol.containsDuplicate([1,2,3,4]))
        