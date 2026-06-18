class Solution:
    def finalValueAfterOperations(self, operations):
        value = 0
        for i in range(len(operations)):
            if "--X" in operations[i] or "X--" in operations[i]:
                value-=1
            if "X++" in operations[i] or "++X" in operations[i]:
                value+=1
        return value

sol = Solution()
print(sol.finalValueAfterOperations(["--X", "X++", "X++"]))