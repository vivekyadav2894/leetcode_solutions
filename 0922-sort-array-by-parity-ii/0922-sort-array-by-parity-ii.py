class Solution(object):
    def sortArrayByParityII(self, nums):
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        nums[0::2] = even
        nums[1::2] = odd

        return nums
       

        