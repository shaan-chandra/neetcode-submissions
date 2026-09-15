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
            if i == "(" or i == "[" or i == "{":
                print("appending to stack: ", i)
                stack.append(i)
            if i in hashmap:
                print("stack here: ", stack)
                if not stack:
                    return False 
                else:
                    item = stack.pop()
                    if item != hashmap[i]:
                        return False
        return stack == []