class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val=nums[0]
        currsum=0

        for i in nums:
            if  currsum <0:
                currsum=0
                
            currsum += i
           
            max_val= max(max_val,currsum)

        return max_val
     
