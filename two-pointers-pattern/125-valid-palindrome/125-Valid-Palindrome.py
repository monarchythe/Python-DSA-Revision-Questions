class Solution:
    def isPalindrome(self, s: str) -> bool:

        i,j = 0, len(s)-1

        while i<j:

            #keep moving i until we found a ALLPA NUM
            while i<j and not s[i].isalnum():
                i+=1
            #keep moving j until we found a ALLPA NUM
            while i<j and not s[j].isalnum():
                j-=1

            #compare 
            if s[i].lower() != s[j].lower():
                return False
            
            i+=1
            j-=1
        
        return True






#String - How to use regex to remove the unwanted character from the sstring
        
        
# - s.isdigit()
# - s.isalpha() 
# — s.isalnum()
# - s.lower()
# - s.upper()

# for PALINDROME QUESTION - do not change the strring first 
# USE SMARTER TECHNIQUE

# OR 
# cleaned_text = ''.join(filter(str.isalnum,s)).lower()

# filter(str.isalnum, s) — goes through each char in s, keeps only those where char.isalnum() returns True. Returns an iterator, not a string.

# ''.join(...) — takes that iterator and joins the chars into a single string with '' (empty) as separator.

# .lower() — lowercases the whole result.

# So "A man, a plan!" → filter keeps ['A','m','a','n','a','p','l','a','n'] → join gives "Amanaplan" → lower gives "amanaplan".

# filter(func, iterable) is a functional-style helper — it's equivalent to (c for c in s if func(c)). str.isalnum here is used as a reference to the method, not called — filter calls it on each char.

