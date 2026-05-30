class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        x = "".join(word1)
        y = "".join(word2)

        if x == y:
            return True
        else:
            return False
        


sol = Solution()
print(sol.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))