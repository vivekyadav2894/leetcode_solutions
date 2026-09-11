class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        ans = []

        for i in range(len(candies)):
            ans.append(candies[i] + extraCandies >= maximum)

        return ans
        
        