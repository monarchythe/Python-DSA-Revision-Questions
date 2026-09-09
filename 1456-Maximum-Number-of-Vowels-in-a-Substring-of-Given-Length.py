class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        i,j = 0,0
        count_v, max_count = 0,0
        vowels = {"a", "e", "i", "o", "u"}

        #buidling till k
        for j in range(k):
            if s[j] in vowels:
                count_v+=1
        
        #record the max / min once at the begining
        max_count = count_v
        
        # rest of the loop 
        for j in range(k, len(s)):

            #shift the fixed window
            if s[j] in vowels:
                count_v +=1
            if s[j-k] in vowels:
                count_v -=1
            
            #keep recoding the max / min at very turn
            max_count = max(max_count, count_v)
        return max_count



# how to create a set of vowels
# i did this - vowels = set("a","e","i","o","u") , ERROR !!!
#you need to do 

#.    vowels = set("aeiou")
#.    vowels = {"a", "e", "i", "o", "u"}


# Also this while inner looping is not REquired

        # while j< len(s):

        #     while j-i+1 <= k:
        #         if s[j] in vowels:
        #             count_v += 1
        #         j+=1
            
        #     max_count = max(max_count, count_v)
            
        #     if s[i] in vowels:
        #         count_v -= 1
        #     i+=1

        # return max_count

# JUST READ THIS :

# Fixed-Width Sliding Window — Complete Notes

# When to use: problem gives you a fixed window size k and asks you to find something within every window of that size.

# Template:

# 1. Build first window (0 to k-1)
# 2. Record answer from first window
# 3. Slide from k to n-1:
#    - Add s[j] (new element entering from right)
#    - Remove s[j-k] (old element leaving from left)
#    - Record answer

# Finding Maximum (e.g., max vowels, max sum of subarray of size k):

# Track your metric as you slide
# max_val = max(max_val, current_metric) after each slide
# Return max_val

# Finding Minimum (e.g., min sum of subarray of size k):

# Exact same template, just flip the comparison
# min_val = min(min_val, current_metric) after each slide
# Return min_val

# Key differences from variable-width:

# No i pointer — the leaving element is always j - k
# No inner while loop — window never grows or shrinks, just slides
# No valid/invalid condition — every window is exactly size k
# One loop (after initial build), O(1) work per step

# One-liner to remember: build once, slide forever — add right, drop left, record.

# vs. variable-width recap:

# Variable: for j + while i + expand/shrink/record
# Fixed: build first window + for j + add/remove/record