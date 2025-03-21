class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        max_P=0
        while r < len(prices):
            
            if(prices[r]>prices[l]):
                diff=prices[r]-prices[l]
                max_P=max(diff,max_P)
            else:
                l=r
            r+=1
        return max_P
        
        