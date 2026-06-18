class Solution:
    def mostWordsFound(self, sentences):
        list1 = []
        for i in range(len(sentences)):
            sent = sentences[i].split(" ")
            list1.append(len(sent))
        return max(list1)

        

sol = Solution()
print(sol.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))