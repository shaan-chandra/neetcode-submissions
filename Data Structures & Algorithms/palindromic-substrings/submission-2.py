class Solution:
    def countSubstrings(self, s: str) -> int:
        # instead of res have count or make res count 
        res = 0
        for i in range(len(s)):
            # odd length palindrome
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            # calculate even length palindrome 
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        print(res)
        return res