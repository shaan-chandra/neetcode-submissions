class Solution:
    def isValid(self, s: str) -> bool:
        # what makes this stack is because we're searching for elements repeated work
        # lets try writing a stack solution
        stack = []
        hashmap = { 
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for i in s:
            if i in hashmap:
                if stack and stack[-1] == hashmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return stack == []