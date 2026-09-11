class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # why did I need a map for this?
        # since it says i can replace with any other uppercase english character my main goal is just to satisfy the condition for k 
        hashmap = {}
        # the algo is count frequency of each character 
        # window_len - char_freq must be < k 
        left, window_len, freq = 0, 0, 0
        # longest repeating measn i need max freq of character
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            #print(hashmap)
            freq = max(freq, hashmap[s[right]])
            #print(freq)
            while (right - left + 1) - freq > k:
                hashmap[s[left]] -= 1
                left += 1
            window_len = max(window_len, (right - left) + 1)
        #print(window_len)
        return window_len
