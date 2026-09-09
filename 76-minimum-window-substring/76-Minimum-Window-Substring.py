class Solution:
    def minWindow(self, s: str, t: str) -> str:

        i = 0
        min_l = float("inf")
        start = 0

        #preparing dict_s
        dict_s = dict()

        #preparing dict_t
        dict_t = dict()
        for item in t:
            dict_t[item] = dict_t.get(item, 0) +1

        #sliding windows loop
        for j in range(len(s)):

            #expand
            dict_s[s[j]] = dict_s.get(s[j],0)+1
            #shring while true + record min_l
            while all(dict_s.get(c,0) >= dict_t[c] for c in dict_t):

                #record compare the lenght
                if j-i+1 < min_l:
                    start = i

                min_l = min(min_l, j-i+1)

                #shrink
                dict_s[s[i]] -= 1
                if dict_s[s[i]] == 0:
                    dict_s.pop(s[i])

                i+=1

        return s[start : start+min_l] if min_l != float("inf") else ""
        

        
#how to add and pop from STRING - IMMUTABLE- 
#slicing : s[start : start+min_l]

#how to compare 2 dictonary? :
# while all(dict_s.get(c,0) >= dict_t[c] for c in dict_t): 

# there is a better way to do that, but if the goal is SPACE COMPLEXITY - MINIMUM , then this solution Beats 99.18 % SOLUTIONS !!!!!!!!!!!!




            

            
        
