class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for i in hashset:
            length = 0
            if i - 1 in hashset:
                continue 
            while i in hashset:
                length += 1
                i += 1
            res = max(length, res)
        return res