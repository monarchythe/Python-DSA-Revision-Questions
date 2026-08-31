class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j=0,0
        max_l,flipped = 0,0

        for j in range(len(nums)):
            # expand: if nums[j] is 0, increment flipped
            if nums[j]==0:
                flipped +=1

            #WHILE for invalid condition 
            while flipped > k:
                if nums[i] == 0:
                    flipped -=1
                i+=1
            
            #recording outside while
            max_l = max(max_l,j-i + 1)

        return max_l


# Always expand first, then shrink. The order is:

# Expand — add nums[j] to your tracking
# Shrink — while invalid
# Record — max_l

# (add to map, then shrink while replacements > k). Always expand → shrink → record. 

# Same order. Always expand → shrink → record. The only difference is where you record:

# Longest valid window: record outside the while (after shrinking stops)
# Shortest valid window: record inside the while (while still valid, before shrinking further)

# The expand → shrink sequence never changes.