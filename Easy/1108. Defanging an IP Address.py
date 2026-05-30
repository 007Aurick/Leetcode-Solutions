class Solution:
    def defangIPaddr(self, address):
        x = address.replace(".", "[.]")
        return x
        


sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))
        