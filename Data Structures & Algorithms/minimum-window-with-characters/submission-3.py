class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, countS = {}, {}
        # first initialise countT
        for i in t:
            countT[i] = countT.get(i,0) + 1
        # initialise sliding window 
        #print(countT)
        left = 0
        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(t)
        for right in range(len(s)):
            countS[s[right]] = countS.get(s[right], 0) + 1
            #print("count s: ", countS)
            if s[right] in countT and countS[s[right]] <= countT[s[right]]:
                have += 1
            # shrinking window condition
            #print("have here: ", have)
            while have == need:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                # move left pointer till window is valid 
                countS[s[left]] -= 1
                if s[left] in countT and countS[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        #print(res, resLen)
        left, right = res[0], res[1]
        return s[left:right+1] if resLen != float("inf") else ""