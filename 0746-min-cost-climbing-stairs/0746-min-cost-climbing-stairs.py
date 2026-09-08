class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range (2,len(cost)):
            now = cost[i] + min(prev1,prev2)
            prev2 = prev1
            prev1 = now

        return (min(prev1,prev2))
