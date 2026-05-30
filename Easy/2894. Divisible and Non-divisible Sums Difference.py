class Solution:
    def differenceOfSums(self, n, m):
        list1 = []
        list2 = []
        for i in range(1,n+1):
            if i % m == 0:
                list1.append(i)

            elif i % m != 0:
                list2.append(i)
                
        return sum(list2)-sum(list1)



sol = Solution()
print(sol.differenceOfSums(10,3))
