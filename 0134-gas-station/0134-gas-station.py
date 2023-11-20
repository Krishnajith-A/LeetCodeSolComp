class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tg=0
        tc=0
        cg=0
        start=0
        for i in range(len(gas)):
            tg+=gas[i]
            tc+=cost[i]
            cg+=gas[i]-cost[i]
            if cg<0:
                start=i+1
                cg=0
        if tg<tc:
            return -1
        else:
            return start%len(gas)
                  
            