class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        list1 = []
        freq = {}
        for i in range(len(str(n))):
            list1.append(int(str(n)[i]))
        
        for x in list1:
            freq[x] = freq.get(x,0)+1

        sum_nums = 0
        for key, values in freq.items():
            sum_nums += (key*values)
        
        return sum_nums





sol = Solution()
print(sol.digitFrequencyScore(122))