import numpy as np
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split("-")

        num1 = int(year)
        num2 = int(month)
        num3 = int(day)

        conv1 = bin(num1)[2:]
        conv2 = bin(num2)[2:]
        conv3 = bin(num3)[2:]

        x = "-".join([conv1,conv2,conv3])

        return x



sol = Solution()
print(sol.convertDateToBinary("2080-02-29"))
        