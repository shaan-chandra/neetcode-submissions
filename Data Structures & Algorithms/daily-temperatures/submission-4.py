class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack solution is easy
        # for stack I need to do-
        stack = []
        res = [0] * len(temperatures)
        for index, value in enumerate(temperatures):
            # stack condition 1) pop, 2) push
            while stack and value > stack[-1][0]:
                item_value, item_index = stack.pop()
                res[item_index] = index - item_index 
            stack.append([value, index])
            #print(stack[-1][0])
            #print(stack)
        #print(res)
        return res