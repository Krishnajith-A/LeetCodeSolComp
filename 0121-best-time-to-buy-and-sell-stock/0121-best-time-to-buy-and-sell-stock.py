class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        mp=prices[0]
        maxp=0
        for p in prices:
            mp=min(p,mp)
            maxp=max(maxp,p-mp)
        return maxp
            
                     
        