class Solution(object):
    def minElement(self, nums):
        x = []
        for i in nums:
            total = sum(int(digits)for digits in str(i))
            x.append(total)
        return min(x)
            
        



        