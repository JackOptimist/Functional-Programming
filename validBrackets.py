def is_valid(s):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []

    def helper(s):
        if not s:
            return True
        elif s[0] in brackets:
            stack.append(s[0])
            return helper(s[1:])
        elif s[0] in brackets.values():
            if not stack or brackets[stack.pop()] != s[0]:
                return False
            return helper(s[1:])
        else:
            return helper(s[1:])

    return helper(s) and not stack

print(is_valid("([]){}"))  
print(is_valid("([)]"))    
print(is_valid("{[()]}")) 
