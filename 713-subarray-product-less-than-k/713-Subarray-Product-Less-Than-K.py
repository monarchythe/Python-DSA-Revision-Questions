class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        i=0
        prod_w = 1
        count = 0

        for j in range(len(nums)):

            #expand the window
            prod_w =  prod_w * nums[j]

            #shrinking while invalid
            while prod_w >= k and i<=j: #the edge case where k never gets less than prod_w
                prod_w = prod_w/nums[i]
                i+=1
            
            #recording 
            count+=j-i+1
        
        return count

        

# The TRICK here is CONTIGUOUS !!!!!!!!!!
# all the SUB ARRAY POSSIBLE 

# HENCE count = count +  ( j-i +1 ) !!!!!!!!!