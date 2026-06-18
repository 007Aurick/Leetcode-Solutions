class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
        list1 = []
        for i in range(len(s)):
            list1.append(s[i])
        
        freq = {}
        for x in list1:
            freq[x] = freq.get(x, 0) + 1
        
        sum_vowels = 0
        sum_const = 0

        for key, val in freq.items():
            if key in vowels:
                if val > sum_vowels:
                    sum_vowels = val
            if key in consonants:
                if val > sum_const:
                    sum_const = val
        
        return sum_vowels + sum_const
       
sol = Solution()
print(sol.maxFreqSum("successes"))