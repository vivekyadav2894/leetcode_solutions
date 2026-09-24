class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for i in s:
            if i in t:
                t = t.replace(i, "", 1)
            else:
                return False
                break
        else:
            return True







   
        
        
      
        