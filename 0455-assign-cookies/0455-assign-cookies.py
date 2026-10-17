class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        x = 0
        y = 0

        while x < len(s) and y < len(g):
            if s[x] >= g[y]:
                y += 1
            x +=1

        return y

        