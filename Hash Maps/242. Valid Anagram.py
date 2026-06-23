class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        list1 = []
        list2 = []
        for i in range(len(s)):
            list1.append(s[i])
        for i in range(len(t)):
            list2.append(t[i])
        for j in list1:
            dict1[j] = dict1.get(j,0)+1
        for j in list2:
            dict2[j] = dict2.get(j,0)+1
            
        if dict1 == dict2:
            return True
        else:
            return False

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
        