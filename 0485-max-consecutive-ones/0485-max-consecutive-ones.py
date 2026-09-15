class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        curr = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > curr:
                    curr = count 
            else:
                count = 0
        return curr 
        
        