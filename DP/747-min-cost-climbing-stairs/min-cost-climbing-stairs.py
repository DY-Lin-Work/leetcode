class Solution:
    def minCost(self, curLevel, cost, sumCost):
        prevLevel = curLevel - 1
        prev2Level = curLevel - 2
        if sumCost[prevLevel] == -1:
            sumCost[prevLevel] = self.minCost(prevLevel, cost, sumCost)
        elif sumCost[prev2Level] == -1:
            sumCost[prev2Level] = self.minCost(prev2Level, cost, sumCost)
        sumCost[curLevel] = min(sumCost[prevLevel] + cost[prevLevel], sumCost[prev2Level] + cost[prev2Level])
        return sumCost[curLevel]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curLevel = len(cost)
        sumCost = [-1]*(curLevel+1)
        sumCost[0] = 0
        sumCost[1] = 0

        return self.minCost(curLevel, cost, sumCost)

            