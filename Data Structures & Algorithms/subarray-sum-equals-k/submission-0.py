class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # map keeps track of prefix sum and count 
        res = 0
        cur = 0
        prefix = {0:1}
        for i in nums:
            cur += i
            diff = cur - k
            res += prefix.get(diff, 0)
            #print("res here: ", res)
            prefix[cur] = prefix.get(cur, 0) + 1
        #print(res)
        return res