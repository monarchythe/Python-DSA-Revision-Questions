class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = []
        i = 0

        for i in range(max(len(word1),len(word2))):

            if i < len(word1):
                merge.append(word1[i])
            if i < len(word2):
                merge.append(word2[i])
        
        return "".join(merge)




## how to join - "".join () - but it takes a iterable
## you cant DO !!! "" + = word[i] as STRINGS ARE IMMUTABLE !!!!

# so i did this code at first -

#         while i < min(len(word1),len(word2)):

#             merge.append(word1[i])
#             merge.append(word2[i])
#             i+=1
        
#         while i < len(word1):
#             merge.append(word1[i])
#             i+=1
#         while i < len(word2):
#             merge.append(word2[i])
#             i+=1
        
#         return "".join(merge)

# but the above one is way smarter, and then this one - 

# from itertools import zip_longest
# return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))