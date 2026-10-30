class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        x=[]
        for i in nums:
            x.append(i * i)
        x.sort()
        return x
        