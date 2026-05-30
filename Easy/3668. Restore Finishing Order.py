class Solution:
    def recoverOrder(self, order, friends):
        list1 = []
        for i in range(len(order)):
            for j in range(len(friends)):
                if order[i] == friends[j]:
                    list1.append(order[i])
        return list1
    

sol = Solution()
print(sol.recoverOrder([3,1,2,5,4], [1,3,4]))