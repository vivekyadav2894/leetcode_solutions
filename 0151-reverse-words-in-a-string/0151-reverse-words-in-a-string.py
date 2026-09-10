class Solution(object):
    def reverseWords(self, s):
        split_s = s.split()
        temp = []
        for i in range(len(split_s)-1, -1, -1):

            temp.append(split_s[i])
            str1 = " ".join(temp)
        return str1
        