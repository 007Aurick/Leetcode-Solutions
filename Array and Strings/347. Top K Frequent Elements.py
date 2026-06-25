class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        list1 = []

        for i in nums:
            dict1[i] = dict1.get(i,0)+1
        
        
    
        count = 0
        while count < k:
            list1.append(max(dict1, key = dict1.get))
            del dict1[max(dict1, key = dict1.get)]
            count+=1
        return list1


sol = Solution()
print(sol.topKFrequent([1], 1))