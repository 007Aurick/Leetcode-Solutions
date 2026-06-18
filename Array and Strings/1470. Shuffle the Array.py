class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1 = []
        list2 = []
        list3 = []

        for i in range(n):
            list1.append(nums[i])
        for i in range(n):
            list2.append(nums[i+n])
    
        list3.append(list1)
        list3.append(list2)

        list4 = []
   
        for i in range(len(list3)-1):
            for j in range(n):
                list4.append(list3[i][j])
                list4.append(list3[i+1][j])

        return list4
              
       
sol = Solution()
print(sol.shuffle([2,5,1,3,4,7],3))