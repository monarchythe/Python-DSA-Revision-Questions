class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        max_l = 0
        chk_set = set()
        
        for j in range(len(s)):

            while s[j] in chk_set:
                chk_set.remove(s[i])
                #current_l -=1
                i+=1

            chk_set.add(s[j])
            #current_l +=1
            max_l = max(max_l, j-i+1)

        return max_l

# So always remember :
    # for longest / largest / maximest  - WINDOW : we will :
    # use inner while loop tp shrink the window till the  condition remains invalid
    # and record lenght outside the inner loop
    # squeeez the window untill it is valid

    # for smallest / minimest - WINDOW : we will :
    # use inner while loop tp shrink the window till the  condition remains valid
    # and record lenght inside the inner loop 
    # squeeez the window untill it breaks/is invalid
                
            