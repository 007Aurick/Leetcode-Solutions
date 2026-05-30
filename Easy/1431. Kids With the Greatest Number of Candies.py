class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_list = []

        for i in range(len(candies)):
            max_list = max(candies)
            if (candies[i] + extraCandies) >= max_list:
                new_list.append(True)
            else:
                new_list.append(False)
        
        return new_list



sol = Solution()

print(sol.kidsWithCandies([2,3,5,1,3], 3))
        