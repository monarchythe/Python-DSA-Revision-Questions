class Solution:
    def maxPower(self, s: str) -> int:

        if len(s)== 1:
            return 1
        
        if len(s)== 0:
            return 0
        
        count=1
        max_c = 0
        
        for i in range(1,len(s)):

            if s[i] == s[i-1]:
                count+=1
            else:
                count = 1

            max_c = max(max_c,count)

        return max_c




