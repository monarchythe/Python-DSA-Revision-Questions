class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

    # """
    # Goal: shortest subarray with sum >= target

    # Outer loop (j): expands window, adds elements

    # Inner while (curr_sum >= target): condition matches the problem's condition — while the window is valid, record length and shrink from the left to see if a smaller valid window exists 
    # or in case of max window, Inner while (curr_sum <= target)

    # Key insight: we shrink while valid, not while invalid. The inner loop is greedy — it keeps squeezing until the window breaks, so the minimum gets captured along the way

    # """
        n = len(nums)
        min_l = float('inf')
        curr_sum = 0

        i,j = 0,0

        while j< n:
            curr_sum = curr_sum + nums[j]

            while curr_sum >= target:
                min_l = min(min_l, j-i+1)
                curr_sum = curr_sum - nums[i]
                i+=1
            
            j+=1
        
        return min_l if min_l != float('inf') else 0




        

            

        