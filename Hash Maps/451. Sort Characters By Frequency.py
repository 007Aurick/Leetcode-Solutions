class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = {}
        list1 = []
        for i in range(len(s)):
            list1.append(s[i])
        list2 = []
        for j in list1:
            dict1[j] = dict1.get(j,0)+1
            
        
        while len(dict1)>0:
            max_key = max(dict1, key = dict1.get)
            occurence = dict1[max_key]
            list2.append(max_key*occurence)
            del dict1[max_key]
            
        return "".join(list2)
        
sol = Solution()
print(sol.frequencySort("tree"))
        