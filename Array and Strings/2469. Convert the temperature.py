class Solution(object):
    def convertTemperature(self, celsius):
        self.celcius = celsius
        kelvin = self.celcius + 273.15
        fahrenheit = self.celcius * 1.80 + 32.00
        ans = [kelvin,fahrenheit]
        return ans
        
sol = Solution()
print(sol.convertTemperature(36.50))

    


    

        