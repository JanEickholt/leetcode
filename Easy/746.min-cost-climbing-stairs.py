def minCostClimbingStairs(cost):
    steps = cost[:2] + [0] * (len(cost) - 2)
    for i in range(2, len(cost)):
        steps[i] = cost[i] + min(steps[i - 1], steps[i - 2])
    return min(steps[-1], steps[-2])