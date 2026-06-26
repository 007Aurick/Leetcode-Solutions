class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d1 = set()
        d2 = set()
        list1 = []
        for i in range(len(A)):
            d1.add(A[i])
            d2.add(B[i])
            list1.append(len(d1&d2))
            
        return list1
        

        

sol = Solution()
print(sol.findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))