class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1 = []
        list2 = []
        list3 = []
        final_list = []
        for i in range(len(nums)):
            if nums[i]< pivot:
                list1.append(nums[i])
            if nums[i] == pivot:
                list2.append(nums[i])
            if nums[i] > pivot:
                list3.append(nums[i])
        
        final_list.append(list1)
        final_list.append(list2)
        final_list.append(list3)

        real_final_list = []

        for i in range(len(final_list)):
            for j in range(len(final_list[i])):
                real_final_list.append(final_list[i][j])

        return real_final_list       
    

sol = Solution()
print(sol.pivotArray([9,12,5,10,14,3,10], 10))