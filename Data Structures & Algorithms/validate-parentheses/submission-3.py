class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        bracket_map = {')':'(', '}':'{', ']':'['}

        stack = []

        for b in s:
            if b in bracket_map:
                if len(stack) == 0 or bracket_map[b] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(b)

        return True if len(stack) == 0 else False