class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0

        if len(s)> len(t):
            return False 

        while i < len(s) and j < len(t):

            if s[i] == t[j]:
                i+=1

            j+=1
        
        return True if i == len(s) else False


        