class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        list1 = []
        dict1 = {}

        for i in range(len(strs)):
            y = "".join(sorted(strs[i]))
            list1.append(y)
        for i in range(len(strs)):
            key = list1[i]
            if key not in dict1:
                dict1[key] = []
            dict1[key].append(strs[i])
        
        
        return list(dict1.values())    
        
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        