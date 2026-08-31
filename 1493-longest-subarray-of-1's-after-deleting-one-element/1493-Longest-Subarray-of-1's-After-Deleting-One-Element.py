class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        flip,i = 0,0
        max_l = 0

        for j in range(len(nums)):

            #expand
            if nums[j]==0:
                flip +=1
            
            #shrink
            while flip > 1:
                if nums[i] == 0:
                    flip -= 1
                i+=1 
            #record lenght
            max_l = max(max_l, j-i+1)

        return max_l-1

# SO this is same as the :

# LC 1004 -> Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's