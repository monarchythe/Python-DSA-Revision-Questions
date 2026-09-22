class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {')': '(', ']': '[', '}': '{'}
        
        stack = []

        for char in s:

            if char in pairs:
                if len(stack) == 0 or stack[-1] != pairs[char]:
                    return False
                
                stack.pop()
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False
            

        
