class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        # condition is without duplicate so if char[i] == 1 duplicate
        # move left window
        # else keep expanding right
        left = 0
        window_len = 0
        count = 0
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
                count -= 1
        # broken condition- while char[i] is 1
            hashset.add(s[right])
            count += 1
            window_len = max(count, window_len)
        print(window_len)
        return window_len

        
        
