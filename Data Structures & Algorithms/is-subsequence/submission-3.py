class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        while r < len(t) and l < len(s):
            while l < len(s) and r < len(t) and s[l] != t[r]:
                r += 1
                continue
            if r >= len(t):
                break 
            print('left: ', l, 'right: ', r) 
            r += 1
            l += 1
        print("left: ", l, "right: ", r)
        return False if l < len(s) else True