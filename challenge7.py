class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        countMax,countMin=1,1
        
        for n in nums:
            tmp=countMax
            countMax=max(n*tmp,n*countMin,n)
            countMin=min(n*tmp,n*countMin,n)

            res=max(res,countMax)
        return countMax
