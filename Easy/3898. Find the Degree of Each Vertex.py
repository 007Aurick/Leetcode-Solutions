class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
      
        list1 = []
    
        for i in range(len(matrix)):
            score = 0
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    score+=1
                else:
                    score+=0
            list1.append(score)
            
        return list1
sol = Solution()
print(sol.findDegrees([[0,1,1],[1,0,1],[1,1,0]]))
                
        